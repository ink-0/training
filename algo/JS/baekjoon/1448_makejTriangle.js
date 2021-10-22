const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

const n = +input.shift();
let sumArr = [];
input = input.map((line) => parseInt(line));
input.sort((a, b) => parseInt(b) - parseInt(a));
// console.log(n, strawArr);

const checkTri = (a, b, c) => {
  return a < b + c;
};

for (let i = 0; i < n - 2; i++) {
  //   console.log('i', i);
  if (checkTri(input[i], input[i + 1], input[i + 2])) {
    ans = [input[i], input[i + 1], input[i + 2]].reduce(
      (acc, cur) => acc + cur
    );
    sumArr.push(ans);
  }
}
console.log(Math.max(...sumArr));
