const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim();
input = Number(input);
let idx = 0;
let ans = 0;
// while (ans <= input) {
//   //   console.log(ans, idx);
//   idx += 1;
//   ans += idx;
// }
// console.log(idx - 1);

for (let i = 1; ans < input; i++) {
  if (ans + i <= input) {
    ans += i;
    idx++;
    // console.log(ans, idx);
  }
  if (ans + i > input) {
    console.log(idx);
    break;
  }
}
