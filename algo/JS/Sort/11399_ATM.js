const fs = require("fs");
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, input] = fs.readFileSync("./test").toString().trim().split("\n");
console.log(n);
console.log(input);

const answer = input
  .split(" ")
  .sort((a, b) => a - b)
  .reduce((acc, cur, i, arr) => acc + cur * (n - i), 0);

console.log(answer);
// numLst = input.split(" ");
// console.log(numLst);

// const reducer = (accumulator, currentValue) => accumulator + currentValue;
// numLst = input.sort((a, b) => a - b);
// console.log(numLst.reduce(reducer));
