const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim();

const numArr = Array.from({ length: parseInt(input) }, (v, i) => i + 1);

while (numArr.length > 1) {
  numArr.shift();
  numArr.push(numArr.shift());
}

console.log(numArr[0]);
