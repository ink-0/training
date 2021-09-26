const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('.');

input.pop();
input.pop();

console.log(input);

const regL = /\[/g;
const regR = /\[/g;
const regl = /\(/g;
const regr = /\)/g;

const ans = input.map((i) => {
  const regLCnt = i.match(regL) ? i.match(regL).length : 0;
  const regRCnt = i.match(regR) ? i.match(regR).length : 0;
  const reglCnt = i.match(regl) ? i.match(regl).length : 0;
  const regrCnt = i.match(regr) ? i.match(regr).length : 0;
  console.log(i, 'i', regLCnt, regRCnt, reglCnt, regrCnt);
  if (regLCnt === regRCnt && reglCnt === regrCnt) return 'yes';
  else return 'no';
});

console.log(ans);
