const fs = require('fs');

let [n, arr] = (fs.readFileSync('./test') + '').toString().trim().split('\n');
arr = arr.split(' ').map((n) => +n);

const isRight = (num) => {
  return num ? true : false;
};
let ans = 0;
let cur = 0;
arr.map((a) => {
  if (isRight(a)) {
    cur += 1;
    ans += cur;
  } else {
    cur = 0;
  }
});
console.log(ans);
