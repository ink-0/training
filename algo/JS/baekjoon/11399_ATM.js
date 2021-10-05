const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync("./test").toString().trim().split("\n");
let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

const line = input[1].split(' ').map(Number);
const sortLine = line.sort((a, b) => a - b);
let ans = 0;
let prev = 0;

sortLine.forEach((l) => {
  prev += l;
  ans += prev;
});

console.log(ans);
