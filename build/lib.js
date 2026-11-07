const d=require('docx');const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,AlignmentType,HeadingLevel,Footer,PageNumber}=d;const F="Arial";
const P=(t,o={})=>new Paragraph({spacing:{after:100},alignment:AlignmentType.JUSTIFIED,indent:o.indent?{left:o.indent}:undefined,children:[new TextRun({text:t,font:F,size:21,bold:o.bold,italics:o.it})]});
const H=t=>new Paragraph({heading:HeadingLevel.HEADING_1,children:[new TextRun(t)]});
const S=t=>new Paragraph({spacing:{before:120,after:60},keepNext:true,children:[new TextRun({text:t,font:F,size:21,bold:true})]});
exports.build=function({file,title,subtitle,a,b,aDef,bDef,sections,footer}){
const c=[];
c.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:60},children:[new TextRun({text:"MEMORANDUM OF UNDERSTANDING",font:F,size:30,bold:true})]}));
c.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:240},children:[new TextRun({text:subtitle,font:F,size:22,bold:true})]}));
c.push(P("Drafting note: Text in [square brackets] is a placeholder to be completed or deleted. Where options are given (“Option A / Option B”), retain one. This template is a starting point only; have it reviewed by a qualified legal adviser in the relevant jurisdiction before signing. Delete this note before use.",{it:true}));
c.push(P("This Memorandum of Understanding (“MoU”) is executed on this [__] day of [Month], [Year] (“Effective Date”)."));
c.push(S("BETWEEN"));c.push(P(aDef));c.push(S("AND"));c.push(P(bDef));
c.push(P(`The ${a} and the ${b} are individually referred to as a “Party” and collectively as the “Parties”.`));
for(const [h,ps] of sections){c.push(H(h));ps.forEach(t=>c.push(/^(Option [A-C]|Schedule)/.test(t)&&t.length<80?S(t):P(t)));}
c.push(new Paragraph({pageBreakBefore:true,heading:HeadingLevel.HEADING_1,children:[new TextRun("SIGNATURES")]}));
const sig=(t,ls)=>{c.push(S(t));ls.forEach(l=>c.push(P(l+": ________________________________")));};
sig(`For and on behalf of the ${a}`,["Name of Entity","Authorised Signatory","Designation","Signature","Date"]);c.push(P("Company Seal, if applicable"));
sig(`For and on behalf of the ${b}`,["Name of Entity","Authorised Signatory","Designation","Signature","Date"]);c.push(P("Company Seal, if applicable"));
c.push(H("WITNESSES"));sig("Witness 1",["Name","Address","Signature"]);sig("Witness 2",["Name","Address","Signature"]);
const doc=new Document({styles:{default:{document:{run:{font:F,size:21}}},paragraphStyles:[{id:"Heading1",name:"Heading 1",basedOn:"Normal",next:"Normal",quickFormat:true,run:{font:F,size:22,bold:true},paragraph:{spacing:{before:240,after:100},keepNext:true,outlineLevel:0}}]},
sections:[{properties:{page:{size:{width:11906,height:16838},margin:{top:1300,bottom:1300,left:1300,right:1300}}},
footer:new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,children:[new TextRun({text:footer+" | Page ",font:F,size:16}),new TextRun({children:[PageNumber.CURRENT],font:F,size:16})]})]}),children:c}]});
return Packer.toBuffer(doc).then(x=>fs.writeFileSync("../"+file,x));};
// shared boilerplate
exports.common=(a,b)=>({
confidentiality:["12. CONFIDENTIALITY",[
`12.1 Each Party shall keep confidential all non-public business, financial, technical, commercial and strategic information received from the other Party (“Confidential Information”) and use it only for the purposes of this MoU.`,
`12.2 Confidential Information may be disclosed only to employees, subcontractors and professional advisers who need to know it and are bound by equivalent confidentiality obligations, or where disclosure is required by law, in which case the disclosing Party shall give prompt notice where lawful.`,
`12.3 These obligations do not apply to information that is publicly available without breach, lawfully known to the receiving Party beforehand, independently developed, or lawfully received from a third party without restriction.`,
`12.4 This clause survives termination for [__] years; trade secrets remain protected for as long as they qualify as such under applicable law.`]],
liability:["14. REPRESENTATIONS AND LIMITATION OF LIABILITY",[
"14.1 Each Party represents that it has the capacity and authority to enter into and perform this MoU.",
"14.2 Neither Party shall be liable to the other for indirect, incidental or consequential loss, including loss of anticipated profit, except to the extent such exclusion is prohibited by law.",
`14.3 Subject to applicable law, each Party's aggregate liability under this MoU shall not exceed [the total fees paid or payable under this MoU in the preceding [__] months / Currency and Amount].`,
"14.4 The limits in this clause do not apply to fraud, wilful misconduct, breach of confidentiality, infringement of intellectual property rights, death or personal injury, or liability that cannot lawfully be limited or excluded."]],
termination:["15. TERMINATION",[
"15.1 Either Party may terminate this MoU by giving [__] days' written notice to the other Party.",
"15.2 Either Party may terminate immediately by written notice if the other Party commits a material breach and fails to remedy it within [__] days of written notice requiring it to do so, or becomes insolvent or subject to winding-up or bankruptcy proceedings.",
`15.3 On termination, the ${a} shall pay all undisputed fees for work properly performed and approved expenses incurred up to the termination date.`,
"15.4 Each Party shall return or securely destroy the other Party's Confidential Information on request, subject to legal retention requirements.",
"15.5 Clauses relating to accrued payment obligations, confidentiality, intellectual property, liability, indemnity, dispute resolution and any others intended to survive shall survive termination."]],
indemnity:["16. INDEMNITY",[
"Each Party shall indemnify the other against direct losses, claims, damages and reasonable legal expenses arising from its fraud, wilful misconduct, material breach of this MoU or violation of applicable law, to the extent attributable to that Party and subject to applicable law."]],
forcemajeure:["17. FORCE MAJEURE",[
"Neither Party shall be liable for delay or failure to perform (other than payment obligations) caused by events beyond its reasonable control, including natural disasters, epidemic, war, riot, government action, or failure of public utilities, provided it gives prompt written notice and uses reasonable efforts to resume performance. If the event continues for more than [__] days, either Party may terminate by written notice."]],
notices:["18. NOTICES",["All notices shall be in writing and sent by email and/or registered post or recognised courier to the addresses below, or any updated address notified in writing.",
`For the ${a}: Name: [Name] | Email: [Email] | Address: [Address]`,
`For the ${b}: Name: [Name] | Email: [Email] | Address: [Address]`,
"Notices sent by email are deemed received when receipt is acknowledged or otherwise evidenced, subject to applicable law."]],
disputes:["19. GOVERNING LAW AND DISPUTE RESOLUTION",[
"19.1 This MoU shall be governed by the laws of [Jurisdiction].",
"19.2 The Parties shall first attempt to resolve any dispute through good-faith discussion within [30] days of written notice of the dispute.",
"19.3 Unresolved disputes shall be referred to arbitration under [applicable arbitration law/rules, e.g. the Arbitration and Conciliation Act, 1996 / institutional rules], as amended, before a sole arbitrator mutually appointed by the Parties (failing agreement, appointed in accordance with applicable law).",
"19.4 The seat and venue of arbitration shall be [City, State, Country] and the language [English].",
"19.5 Courts at [City, State] shall have jurisdiction over matters for which court jurisdiction is available."]],
general:["20. GENERAL PROVISIONS",[
"20.1 This MoU is the entire understanding between the Parties on its subject matter and supersedes prior discussions.",
"20.2 Amendments must be in writing and signed by both Parties.",
"20.3 Neither Party may assign or subcontract its rights or obligations without the other's prior written consent, except as expressly permitted in this MoU.",
"20.4 If any provision is held invalid or unenforceable, the remainder continues in effect to the extent legally permissible.",
"20.5 No failure or delay in exercising a right operates as a waiver of it.",
"20.6 This MoU may be executed in counterparts and by legally valid electronic signatures, where permitted by applicable law.",
"20.7 The Parties shall ensure payment of stamp duty and compliance with execution formalities under applicable law.",
"20.8 The Parties intend this MoU to create legally binding obligations, subject to applicable law."]]});
