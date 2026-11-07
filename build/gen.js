const d=require('docx');const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,AlignmentType,HeadingLevel,Footer,PageNumber,LevelFormat}=d;
const F="Arial";
const P=(t,o={})=>new Paragraph({spacing:{after:100},alignment:AlignmentType.JUSTIFIED,indent:o.indent?{left:o.indent}:undefined,children:[new TextRun({text:t,font:F,size:21,bold:o.bold,italics:o.it})]});
const H=t=>new Paragraph({heading:HeadingLevel.HEADING_1,children:[new TextRun(t)]});
const S=(t)=>new Paragraph({spacing:{before:120,after:60},keepNext:true,children:[new TextRun({text:t,font:F,size:21,bold:true})]});
const sub=t=>P(t,{indent:360});
const c=[];
c.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:60},children:[new TextRun({text:"MEMORANDUM OF UNDERSTANDING",font:F,size:30,bold:true})]}));
c.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:240},children:[new TextRun({text:"For Consultancy Services for [Fundraising Stage, e.g. Pre-Seed / Seed / Series A] Fundraising",font:F,size:22,bold:true})]}));
c.push(P("Drafting note: Text in [square brackets] is a placeholder to be completed or deleted. Where options are given (marked “Option A / Option B”), retain one. This template is a starting point only and should be reviewed by a qualified legal adviser in the relevant jurisdiction before signing.",{it:true}));
c.push(P("This Memorandum of Understanding (“MoU”) is executed on this [__] day of [Month], [Year] (“Effective Date”)."));
c.push(S("BETWEEN"));
c.push(P("[Company Legal Name], a company incorporated under [applicable Companies Act / law], having its registered office at [Registered Office Address], registration/CIN no. [Registration Number], acting through its authorised signatory [Name], [Designation], hereinafter referred to as the “Company” (which expression shall, unless repugnant to the context, include its successors and permitted assigns);"));
c.push(S("AND"));
c.push(P("[Consultant Name / Firm Name], [an individual / a firm / a company] having its address at [Consultant Address], [PAN / Tax ID: ________], [represented by [Name], if applicable], hereinafter referred to as the “Consultant” (which expression shall, unless repugnant to the context, include its permitted successors and assigns)."));
c.push(P("The Company and the Consultant are individually referred to as a “Party” and collectively as the “Parties”."));
const sections=[
["1. PURPOSE OF THE MoU",[
"The Company intends to raise [stage] capital to support its business operations, product development, market expansion and other business objectives.",
"The Company hereby engages the Consultant to provide consultancy and fundraising support services, subject to the terms and conditions contained in this MoU.",
"The target fundraising amount shall be approximately [Currency and Amount in figures and words], or such other amount as may be mutually agreed upon in writing (“Target Amount”)."]],
["2. SCOPE OF SERVICES",["The Consultant shall provide the following services:",
"a. Assist in identifying and preparing a list of suitable investors, such as angel investors, venture capital funds, family offices, incubators, accelerators and other potential funding sources.",
"b. Facilitate introductions to prospective investors, subject to their interest and availability.",
"c. Assist the Company in preparing for investor meetings, presentations, due diligence and fundraising discussions.",
"d. Provide feedback on investor questions, valuation expectations, fundraising strategy and proposed investment structures.",
"e. Assist in coordinating communications between the Company and prospective investors.",
"f. Provide reasonable follow-up support during investor discussions and the fundraising process.",
"g. Assist with the preparation and organisation of information required for investor due diligence, in coordination with the Company's legal, financial and tax advisers.",
"h. [Any additional services, or “Not applicable”.]",
"The Consultant shall not be responsible for independently certifying the Company's financial statements, legal compliance or statutory filings."]],
["3. NATURE OF ENGAGEMENT",[
"3.1 The Consultant shall act as an independent consultant. Nothing in this MoU shall create an employer-employee relationship, partnership, joint venture or general agency between the Parties.",
"3.2 The Consultant shall not have authority to bind the Company, execute agreements on its behalf, accept investment commitments, or negotiate or finalise investment terms without the Company's prior written authorisation.",
"3.3 The Consultant shall not guarantee that any investor will invest in the Company or that the Target Amount will be achieved.",
"3.4 All investment decisions shall remain at the sole discretion of the Company and the prospective investors.",
"3.5 The engagement is [non-exclusive / exclusive for the term of this MoU] unless the Parties expressly agree otherwise in writing."]],
["4. DURATION",[
"This MoU shall commence on the Effective Date and remain in force for a period of [__] months, unless terminated earlier in accordance with this MoU.",
"The Parties may extend the term by mutual written agreement."]],
["5. CONSULTANCY FEES AND PAYMENT TERMS",[
"The Parties shall select and complete one commercial arrangement below and delete the other(s).",
"Option A – Success-Based Fee",
"Subject to applicable laws and regulatory requirements, the Company shall pay the Consultant a success fee of [__]% of the qualifying funds, raised in tranches, actually received by the Company from investors introduced by, or demonstrably facilitated through, the Consultant during the term of this MoU. For this purpose:",
"a. The success fee shall be calculated on the tranche amount actually credited to the Company's designated bank account, excluding amounts merely committed, proposed or discussed.",
"b. The fee shall become payable within [__] business days after the relevant funds are received by the Company.",
"c. The fee shall apply only to investors and transactions falling within the agreed scope and attribution criteria (Clause 9).",
"d. Any fee relating to subsequent investment tranches, follow-on investments or transactions completed after termination must be expressly agreed in writing.",
"e. Applicable indirect taxes, withholding taxes and other statutory deductions shall be handled in accordance with applicable law.",
"Option B – Fixed / Retainer Fee",
"The Company shall pay the Consultant a [monthly / one-time] fee of [Currency and Amount], payable [on the first day of each month / on the dates set out in a payment schedule], exclusive of applicable taxes.",
"Option C – Hybrid",
"The Company shall pay the Consultant (i) a retainer of [Currency and Amount] per [month], and (ii) a success fee of [__]% calculated and payable in accordance with Option A above. [Specify whether retainer is creditable against the success fee.]"]],
["6. EXPENSES",[
"The Consultant shall bear its ordinary business expenses.",
"Any extraordinary expenses, including travel, accommodation, event participation or third-party professional services, shall be pre-approved in writing by the Company and reimbursed [promptly on submission of supporting documents / only after successful disbursement of funds], subject to a maximum of [__]% of the tranche amount received by the Company [or a fixed cap of Currency and Amount], supported by reasonable documentary evidence."]],
["7. OBLIGATIONS OF THE COMPANY",["The Company agrees to:",
"a. Provide accurate, complete and timely information reasonably required for the consultancy services.",
"b. Ensure that information supplied to prospective investors is not knowingly false, misleading or materially incomplete.",
"c. Make its founders and relevant team members reasonably available for investor meetings and discussions.",
"d. Review and approve all material investor-facing communications and documents before circulation.",
"e. Appoint appropriate legal, accounting, tax and other professional advisers where necessary.",
"f. Make all investment, valuation, capital structure and transaction decisions independently.",
"g. Pay the Consultant's agreed fees and approved expenses in accordance with this MoU."]],
["8. OBLIGATIONS OF THE CONSULTANT",["The Consultant agrees to:",
"a. Perform the services with reasonable care, skill and diligence.",
"b. Act honestly and professionally in dealings with the Company and prospective investors.",
"c. Maintain reasonable records of investor introductions and material fundraising activities.",
"d. Not make unauthorised representations, guarantees or commitments on behalf of the Company.",
"e. Disclose any material conflict of interest relevant to the engagement.",
"f. Not accept undisclosed commissions, referral payments or other benefits in connection with the Company's fundraising.",
"g. Comply with applicable laws and refrain from undertaking any activity requiring a regulatory registration, licence or authorisation unless duly authorised to do so.",
"h. Keep the Company reasonably informed about the progress of the agreed activities."]],
["9. INVESTOR INTRODUCTIONS AND ATTRIBUTION",[
"9.1 The Consultant may maintain a written list of prospective investors introduced to the Company.",
"9.2 An investor shall be considered a Consultant-introduced investor only where the introduction or material facilitation can reasonably be evidenced through emails, messages, meeting records or other written documentation.",
"9.3 Investors with whom the Company had an active, documented fundraising discussion before the Consultant's introduction shall be excluded unless the Parties agree otherwise in writing.",
"9.4 Any post-termination success fee or protection period shall apply only if expressly agreed in writing. If agreed, the period shall be [__] months after termination and shall cover only qualifying investors introduced during the engagement.",
"9.5 No fee shall be payable twice for the same funds, and no success fee shall be payable where prohibited by applicable law."]],
["10. CONFIDENTIALITY",[
"10.1 Each Party shall keep confidential all non-public business, financial, technical, commercial, investor-related and strategic information received from the other Party.",
"10.2 Confidential information shall be used only for the purposes of this engagement and shall not be disclosed to third parties without prior written consent, except to professional advisers who are bound by confidentiality obligations or where disclosure is required by law.",
"10.3 The Consultant shall not disclose the Company's pitch deck, financial projections, business plans, customer information, intellectual property or fundraising status to prospective investors except as authorised by the Company.",
"10.4 These obligations shall not apply to information that is publicly available without breach, lawfully known to the receiving Party beforehand, independently developed, or lawfully received from a third party without a confidentiality restriction.",
"10.5 The confidentiality obligations shall survive termination for [__] years, and trade secrets shall remain protected for as long as they qualify as trade secrets under applicable law."]],
["11. INTELLECTUAL PROPERTY",[
"11.1 All pre-existing intellectual property, methodologies, templates, know-how and proprietary materials of either Party shall remain the property of that Party.",
"11.2 Upon full payment of the applicable fees, deliverables specifically created for the Company under this engagement, including its customised pitch deck, financial model and fundraising materials, shall belong to the Company, subject to third-party rights and the Consultant's pre-existing intellectual property.",
"11.3 The Consultant shall not reuse or disclose the Company's confidential information or proprietary business materials for another client without the Company's prior written consent."]],
["12. COMPLIANCE AND NO AUTHORITY TO HANDLE INVESTOR FUNDS",[
"12.1 The Parties shall comply with applicable laws of [Jurisdiction], including relevant corporate, securities, tax, foreign exchange and data protection requirements, as applicable to their respective activities.",
"12.2 The Consultant shall not receive, hold, pool or transfer investor funds on behalf of the Company or any investor.",
"12.3 The Consultant shall not provide regulated investment advice, undertake securities distribution, act as a placement agent or perform other regulated financial activities unless appropriately authorised and legally permitted to do so.",
"12.4 Any proposed success-based compensation or investor solicitation activity shall be reviewed for regulatory compliance before it is undertaken. If the agreed fee structure or scope is not legally permissible, the Parties shall amend it in writing to a lawful arrangement.",
"12.5 The Company shall retain responsibility for the legality of the fundraising instrument, corporate approvals, required disclosures, allotments and statutory filings, with support from its appointed professional advisers."]],
["13. REPRESENTATIONS AND LIMITATION OF LIABILITY",[
"13.1 Each Party represents that it has the capacity and authority to enter into this MoU.",
"13.2 The Consultant does not warrant any minimum fundraising amount, investor response, valuation, closing date or investment outcome.",
"13.3 Neither Party shall be liable to the other for indirect, incidental or consequential losses, including loss of anticipated profits, except to the extent such exclusion is prohibited by law.",
"13.4 Subject to applicable law, neither Party's aggregate liability arising from this MoU shall exceed the total consultancy fees paid or payable under this MoU during the preceding [__] months.",
"13.5 The limitation in Clause 13.4 shall not apply to fraud, wilful misconduct, breach of confidentiality, infringement of intellectual property rights, or liability that cannot lawfully be limited or excluded."]],
["14. TERMINATION",[
"14.1 Either Party may terminate this MoU by giving [__] days' written notice to the other Party.",
"14.2 Either Party may terminate this MoU immediately by written notice if the other Party commits a material breach and fails to remedy it within [__] days after receiving written notice requiring it to do so.",
"14.3 Upon termination, the Company shall pay all undisputed fees for services performed up to the termination date and approved expenses incurred before termination.",
"14.4 Any success fee after termination shall be payable only to the extent expressly provided under Clause 9 and legally permissible.",
"14.5 Each Party shall return or securely destroy the other Party's confidential information upon request, subject to legal retention requirements.",
"14.6 Clauses relating to accrued payment obligations, confidentiality, intellectual property, liability, dispute resolution and any expressly surviving success-fee obligations shall survive termination to the extent applicable."]],
["15. INDEMNITY",[
"Each Party shall indemnify the other against direct losses, claims, damages and reasonable legal expenses arising from its fraud, wilful misconduct, material breach of this MoU or violation of applicable law, to the extent attributable to that Party and subject to applicable law.",
"Neither Party shall be responsible for losses caused by the other Party's independent acts, omissions or unauthorised representations."]],
["16. RELATIONSHIP WITH INVESTORS",[
"The Consultant shall not have authority to bind the Company or any investor to an investment transaction.",
"All investment agreements, subscription documents, shareholders' agreements, convertible instruments and other transaction documents shall be negotiated, approved and executed by the relevant parties through their authorised representatives and professional advisers.",
"The Consultant shall not represent that any investor has committed to invest unless such commitment is duly documented and authorised."]],
["17. NOTICES",["All notices under this MoU shall be sent by email and/or registered post or recognised courier to the addresses set out below, or to any updated address notified in writing."]],
];
for(const [h,ps] of sections){c.push(H(h));ps.forEach(t=>{ if(/^Option [ABC]/.test(t)) c.push(S(t)); else c.push(P(t));});}
// notices
for(const w of ["For the Company","For the Consultant"]){c.push(S(w));["Name: [Name]","Email: [Email Address]","Address: [Address]"].forEach(t=>c.push(P(t)));}
c.push(P("Notices sent by email shall be deemed received when receipt is acknowledged or otherwise evidenced, subject to applicable law."));
const tail=[
["18. GOVERNING LAW AND DISPUTE RESOLUTION",[
"18.1 This MoU shall be governed by the laws of [Jurisdiction].",
"18.2 The Parties shall first attempt to resolve any dispute through good-faith discussions within [30] days of written notice of the dispute.",
"18.3 If the dispute remains unresolved, it shall be referred to arbitration under [applicable arbitration law/rules, e.g. the Arbitration and Conciliation Act, 1996 / institutional rules], as amended.",
"18.4 The arbitration shall be conducted by a sole arbitrator mutually appointed by the Parties. If the Parties cannot agree on the arbitrator, the appointment shall be made in accordance with applicable law.",
"18.5 The seat and venue of arbitration shall be [City, State, Country]. The proceedings shall be conducted in [English].",
"18.6 Courts at [City, State] shall have jurisdiction over matters for which court jurisdiction is available, subject to applicable law."]],
["19. GENERAL PROVISIONS",[
"19.1 This MoU constitutes the entire understanding between the Parties concerning the subject matter and supersedes prior discussions relating to the same.",
"19.2 Any amendment shall be made in writing and signed by both Parties.",
"19.3 Neither Party may assign its rights or obligations under this MoU without the prior written consent of the other Party, except as otherwise agreed in writing.",
"19.4 If any provision is held invalid or unenforceable, the remaining provisions shall continue in effect to the extent legally permissible.",
"19.5 This MoU may be executed in counterparts and through legally valid electronic signatures, where permitted by applicable law.",
"19.6 The Parties shall ensure appropriate stamp duty and execution formalities under the applicable law of the relevant jurisdiction.",
"19.7 The Parties intend this MoU to create legally binding obligations in respect of the consultancy engagement, subject to applicable law."]]];
for(const [h,ps] of tail){c.push(H(h));ps.forEach(t=>c.push(P(t)));}
const sig=(title,lines)=>{c.push(S(title));lines.forEach(l=>c.push(P(l+": ________________________________")));};
c.push(new Paragraph({pageBreakBefore:true,heading:HeadingLevel.HEADING_1,children:[new TextRun("SIGNATURES")]}));
sig("For and on behalf of the Company",["Company Name","Authorised Signatory","Designation","Signature","Date"]);
c.push(P("Company Seal, if applicable"));
sig("For and on behalf of the Consultant",["Consultant Name","Authorised Signatory, if applicable","Designation","Signature","Date"]);
c.push(new Paragraph({heading:HeadingLevel.HEADING_1,children:[new TextRun("WITNESSES")]}));
sig("Witness 1",["Name","Address","Signature"]);sig("Witness 2",["Name","Address","Signature"]);
const doc=new Document({styles:{default:{document:{run:{font:F,size:21}}},paragraphStyles:[{id:"Heading1",name:"Heading 1",basedOn:"Normal",next:"Normal",quickFormat:true,run:{font:F,size:22,bold:true},paragraph:{spacing:{before:240,after:100},keepNext:true,outlineLevel:0}}]},
sections:[{properties:{page:{size:{width:11906,height:16838},margin:{top:1300,bottom:1300,left:1300,right:1300}}},
footer:new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,children:[new TextRun({text:"MoU – Fundraising Consultancy Services | Page ",font:F,size:16}),new TextRun({children:[PageNumber.CURRENT],font:F,size:16})]})]}),children:c}]});
Packer.toBuffer(doc).then(b=>fs.writeFileSync("Fundraising_Consultancy_MoU_Template.docx",b));
