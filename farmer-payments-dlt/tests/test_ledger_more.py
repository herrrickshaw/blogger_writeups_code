import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from fpdlt.ledger import GENESIS, Ledger, LedgerError, _h  # noqa: E402


def make():
    L = Ledger()
    for org in ("FPO-1", "AgriBank", "Agency", "Arbiter"):
        L.register(org, org.encode() + b"-secret")
    return L


def rehash(b):
    b["hash"] = _h({k: b[k] for k in ("index", "ts", "prev", "payload", "sig")})


class Chain(unittest.TestCase):
    def test_empty_chain_verifies_and_first_block_links_to_genesis(self):
        L = make()
        self.assertTrue(L.verify())
        b = L.append("Agency", "k", {})
        self.assertEqual(b["prev"], GENESIS)
        self.assertEqual(b["index"], 0)
        b2 = L.append("Agency", "k", {})
        self.assertEqual((b2["prev"], b2["index"]), (b["hash"], 1))

    def test_wrong_prev_link_detected_even_when_hash_recomputed(self):
        L = make()
        L.append("Agency", "a", {})
        L.append("Agency", "b", {})
        L.blocks[1]["prev"] = "f" * 64
        rehash(L.blocks[1])
        self.assertFalse(L.verify())

    def test_wrong_index_detected(self):
        L = make()
        L.append("Agency", "a", {})
        L.blocks[0]["index"] = 5
        rehash(L.blocks[0])
        self.assertFalse(L.verify())

    def test_forged_signature_detected_even_when_hash_recomputed(self):
        L = make()
        L.append("Agency", "a", {"x": 1})
        L.blocks[0]["payload"]["data"]["x"] = 2        # edit
        rehash(L.blocks[0])                              # attacker fixes the hash but cannot sign
        self.assertFalse(L.verify())

    def test_block_attributed_to_unregistered_org_fails(self):
        L = make()
        L.append("Agency", "a", {})
        del L.members["Agency"]
        self.assertFalse(L.verify())

    def test_signature_is_per_org_secret(self):
        L = make()
        L.append("Agency", "a", {})
        L.members["Agency"] = b"rotated"
        self.assertFalse(L.verify())

    def test_non_member_error_names_org_and_appends_nothing(self):
        L = make()
        with self.assertRaisesRegex(LedgerError, "Mallory is not a consortium member"):
            L.append("Mallory", "x", {})
        self.assertEqual(L.blocks, [])


class Escrow(unittest.TestCase):
    def test_duplicate_id_and_nonpositive_amount_rejected_without_side_effects(self):
        L = make()
        L.open_escrow("FPO-1", "E1", "F1", 10, "B")
        with self.assertRaisesRegex(LedgerError, "duplicate escrow id"):
            L.open_escrow("FPO-1", "E1", "F1", 10, "B")
        for amt in (0, -5):
            with self.assertRaisesRegex(LedgerError, "amount must be positive"):
                L.open_escrow("FPO-1", "E2", "F1", amt, "B")
        self.assertEqual(len(L.blocks), 1) and self.assertNotIn("E2", L.escrows)

    def test_grade_boundary_best_is_a(self):
        for grade, want in (("A", "RELEASED"), ("B", "RELEASED"), ("C", "DISPUTED")):
            L = make()
            L.open_escrow("FPO-1", "E", "F", 10, "B")
            self.assertEqual(L.confirm_delivery("FPO-1", "E", grade, 1), want)
            self.assertEqual(L.escrows["E"]["state"], want)
            self.assertEqual(L.blocks[-1]["payload"]["kind"], "escrow_" + want.lower())

    def test_state_machine_guards(self):
        L = make()
        with self.assertRaisesRegex(LedgerError, "unknown escrow"):
            L.confirm_delivery("FPO-1", "nope", "A", 1)
        L.open_escrow("FPO-1", "E", "F", 10, "B")
        with self.assertRaisesRegex(LedgerError, "expected DISPUTED"):
            L.resolve_dispute("Arbiter", "E", 50)            # not disputed yet
        L.confirm_delivery("FPO-1", "E", "A", 1)
        with self.assertRaisesRegex(LedgerError, "escrow is RELEASED, expected FUNDED"):
            L.confirm_delivery("FPO-1", "E", "A", 1)         # no double release

    def test_resolve_dispute_pct_bounds(self):
        for pct, ok in ((-0.01, False), (0, True), (100, True), (100.01, False)):
            L = make()
            L.open_escrow("FPO-1", "E", "F", 10, "B")
            L.confirm_delivery("FPO-1", "E", "C", 1)
            if ok:
                L.resolve_dispute("Arbiter", "E", pct)
                self.assertEqual(L.escrows["E"]["state"], "SETTLED")
            else:
                with self.assertRaisesRegex(LedgerError, "pct out of range"):
                    L.resolve_dispute("Arbiter", "E", pct)
                self.assertEqual(L.escrows["E"]["state"], "DISPUTED")


class Disburse(unittest.TestCase):
    def test_unverified_checked_before_duplicate_and_does_not_burn_the_slot(self):
        L = make()
        with self.assertRaisesRegex(LedgerError, "not verified"):
            L.disburse("Agency", "S", "P", "F", 5, False)
        L.disburse("Agency", "S", "P", "F", 5, True)         # slot was not consumed by the failed attempt
        with self.assertRaisesRegex(LedgerError, "duplicate disbursement"):
            L.disburse("Agency", "S", "P", "F", 5, True)

    def test_non_member_agency_does_not_consume_slot_state_incorrectly(self):
        L = make()
        with self.assertRaises(LedgerError):
            L.disburse("Mallory", "S", "P", "F", 5, True)
        self.assertEqual(L.blocks, [])


class Reconcile(unittest.TestCase):
    def test_partial_credit_exact_credit_and_overpayment(self):
        L = make()
        L.open_escrow("FPO-1", "E", "F1", 1000, "B")
        L.confirm_delivery("FPO-1", "E", "A", 1)
        L.disburse("Agency", "S", "P", "F2", 500.5, True)
        L.disburse("Agency", "S", "P", "F3", 100, True)
        out = L.reconcile({"F1": 400.25, "F2": 500.5, "F3": 150})
        self.assertEqual(out, {"F1": 599.75})

    def test_disputed_and_unreleased_escrows_owe_nothing(self):
        L = make()
        L.open_escrow("FPO-1", "E", "F1", 1000, "B")
        self.assertEqual(L.reconcile({}), {})
        L.confirm_delivery("FPO-1", "E", "C", 1)
        self.assertEqual(L.reconcile({}), {})

    def test_multiple_payments_to_one_farmer_accumulate(self):
        L = make()
        L.disburse("Agency", "S", "P1", "F", 100, True)
        L.disburse("Agency", "S", "P2", "F", 50, True)
        self.assertEqual(L.reconcile({"F": 20}), {"F": 130})


if __name__ == "__main__":
    unittest.main()
