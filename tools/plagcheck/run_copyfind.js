#!/usr/bin/env node
// WCopyfind/CopyFind-equivalent pass (via pl-copyfind), the phrase-level
// confirmation step for pairs JPlag already flagged as similar. JPlag scores
// structural similarity fast across all pairs; this reports the actual
// matched phrases so a human can see what's really shared, the way
// WCopyfind's own report does.
const fs = require('fs');
const path = require('path');
const copyfind = require('./node_copyfind/node_modules/pl-copyfind');

const [,, csvPath, txtDir, outPath] = process.argv;
if (!csvPath || !txtDir || !outPath) {
  console.error('usage: node run_copyfind.js <jplag-results.csv> <txt-dir> <out.json>');
  process.exit(1);
}

const rows = fs.readFileSync(csvPath, 'utf8').trim().split('\n').slice(1)
  .map(line => {
    const [a, b, avg, max] = line.split(',');
    return { a, b, avg: parseFloat(avg), max: parseFloat(max) };
  })
  .filter(r => r.max >= 0.15);

const options = { PhraseLength: 6, WordThreshold: 15, bIgnoreCase: true, bBuildReport: false };

let i = 0;
const results = [];
function next() {
  if (i >= rows.length) {
    fs.writeFileSync(outPath, JSON.stringify(results, null, 2));
    console.log(`wrote ${results.length} pair reports to ${outPath}`);
    return;
  }
  const row = rows[i++];
  const textA = fs.readFileSync(path.join(txtDir, row.a), 'utf8');
  const textB = fs.readFileSync(path.join(txtDir, row.b), 'utf8');
  copyfind(textA, textB, options, (err, data) => {
    if (!err && data.matches.length) {
      const sample = data.matches.slice(0, 3).map(m => textB.substr(m.textR.pos, m.textR.length));
      results.push({ a: row.a, b: row.b, jplagMax: row.max, phraseMatches: data.matches.length, sample });
    }
    next();
  });
}
next();
