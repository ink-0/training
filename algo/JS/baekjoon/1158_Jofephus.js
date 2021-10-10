const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split(' ');

let n = parseInt(input[0]);
let k = parseInt(input[1]);
let arr = [];
let answer = '';
let deleted = [];
for (let i = 0; i < n; i++) {
  arr[i] = i + 1;
}
for (j = 0; j < n; j++) {
  for (let m = 1; m <= k; m++) {
    if (m === k) {
      deleted.push(arr.shift());
    } else {
      arr.push(arr.shift());
    }
  }
}
answer = '<' + deleted.join(', ') + '>';
console.log(answer);
