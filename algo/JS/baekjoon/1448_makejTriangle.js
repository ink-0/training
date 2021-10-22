const fs = require('fs');

let input = (fs.readFileSync('./dev/stdin') + '').toString().trim().split('\n');
const n = +input.shift();
input = input.map((a) => parseInt(a)).sort((a, b) => b - a);
let ans = 0;
const checkTri = (a, b, c) => {
  return a < b + c;
};

for (let i = 0; i < n - 2; i++) {
  if (checkTri(input[i], input[i + 1], input[i + 2])) {
    ans = [input[i], input[i + 1], input[i + 2]].reduce(
      (acc, cur) => acc + cur
    );
    break;
  }
}

console.log(ans === 0 ? -1 : ans);
