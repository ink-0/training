const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync("./test").toString().trim().split("\n");

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

const turnCnt = Math.max(...input.map((i) => i.length));

let ans = '';

for (let i = 0; i < turnCnt; i++) {
  for (let j = 0; j < input.length; j++) {
    ans += input[j][i] || '';
  }
}

console.log(ans);
