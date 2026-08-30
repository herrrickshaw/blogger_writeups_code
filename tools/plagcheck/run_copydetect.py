#!/usr/bin/env python3
"""Third similarity signal: copydetect's winnowing/document-fingerprinting
algorithm (same family as MOSS), run over the same boilerplate-stripped
corpus JPlag and pl-copyfind already check. A different algorithm family
catches different false-negatives than the other two.

Run via the venv this needs: ~/.venvs/masaladeutsch-plagcheck/bin/python3
"""
import csv, json, sys
from copydetect import CopyDetector


def main():
    txt_dir, out_csv = sys.argv[1], sys.argv[2]
    detector = CopyDetector(
        test_dirs=[txt_dir], ref_dirs=[txt_dir], extensions=['txt'],
        display_t=0.15, autoopen=False, silent=True,
        # copydetect's default cross-file filtering flags nearly everything
        # as "boilerplate" on a 183-file corpus and returns zero matches;
        # disabling it and requiring a longer run (25 tokens, the library's
        # own default) instead is what actually surfaces real matches here.
        noise_t=25, guarantee_t=25, disable_filtering=True,
    )
    detector.run()
    rows = detector.get_copied_code_list()
    with open(out_csv, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['testSimilarity', 'refSimilarity', 'testFile', 'refFile', 'overlappingTokens'])
        seen = set()
        for test_sim, ref_sim, test_path, ref_path, *_rest, tokens in rows:
            a, b = sorted([test_path.split('/')[-1], ref_path.split('/')[-1]])
            if (a, b) in seen:
                continue
            seen.add((a, b))
            w.writerow([f'{test_sim:.3f}', f'{ref_sim:.3f}', a, b, tokens])
    print(f'wrote {len(seen)} pairs to {out_csv}')


if __name__ == '__main__':
    main()
