const fs = require('fs');

let n = (fs.readFileSync('./test') + '').toString().trim();
n = Number(n);

const DP = new Array(n + 1).fill(0);

for (let i = 2; i <= n; i++) {
  DP[i] = DP[i - 1] + 1;

  if (i % 2 === 0) DP[i] = Math.min(DP[i], DP[i / 2] + 1);
  if (i % 3 === 0) DP[i] = Math.min(DP[i], DP[i / 3] + 1);
}
console.log(DP[n]);
