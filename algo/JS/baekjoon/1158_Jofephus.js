const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split(' ');
let [n, k] = input.map((n) => parseInt(n));
let ansArr = [];
const arr = Array.from({ length: n }, (v, i) => i + 1);

// for (let i = 0; i < n; i++) {
//   for (let j = 1; j <= k; j++) {
//     if (j === k) {
//       ansArr.push(arr.shift());
//     } else {
//       arr.push(arr.shift());
//     }
//   }
// }

// const ans = '<' + ansArr.join(', ') + '>';
// console.log(ans);

let cnt = 0;

while (arr.length > 0) {
  cnt = (cnt + k - 1) % arr.length;
  ansArr.push(arr[cnt]);
  arr.splice(cnt, 1);
}
const ans = '<' + ansArr.join(', ') + '>';
console.log(ans);
