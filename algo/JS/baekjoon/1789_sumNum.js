const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim();
input = Number(input);
// let idx = 0;
// let ans = 0;
// while (ans < input) {
//   idx += 1;
//   ans += idx;
// }

for (let i = 1; ans < input; i++) {
  if (ans + i <= input) {
    sum += i;
    idx++;
  }
  if (sum + i > input) {
    console.log(cnt);
    break;
  }
}

console.log(idx - 1);
