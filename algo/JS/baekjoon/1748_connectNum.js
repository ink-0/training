const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim();
const lenInput = input.length;
let cnt = 0;

// 1     2      3
// 10-1 100-10 + 120-(100-1)
// for (let i = 1; i <= lenInput; i++) {
//   if (i === lenInput) {
//     let curCnt = (parseInt(input) - (10 ** (i - 1) - 1)) * i;

//     cnt += curCnt;
//   } else {
//     let curCnt = (10 ** i - 10 ** (i - 1)) * i;
//     cnt += curCnt;
//   }
// }

let cnt = 0;
for (let i = 1; i <= N; i *= 10) {
  cnt += N - i + 1;
}

console.log(cnt);
