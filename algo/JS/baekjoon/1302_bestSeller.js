const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

input.shift();

let bookDict = {};

input.map((book) => {
  if (!bookDict[book]) bookDict[book] = 1;
  else bookDict[book] += 1;
});

const sortBook = Object.entries(bookDict)
  .sort(([aa, a], [bb, b]) => {
    if (a === b) {
      return aa < bb ? -1 : aa == bb ? 0 : 1;
    }
    return b - a;
  })
  .reduce((r, [k, v]) => ({ ...r, [k]: v }), {});

console.log(Object.keys(sortBook)[0]);
