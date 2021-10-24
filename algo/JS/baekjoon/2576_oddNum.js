const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

let oddArr = [];
let sumOdd = 0;

input.map((num) => {
  if (+num % 2 !== 0) {
    oddArr.push(+num);
    sumOdd += +num;
  }
});

if (oddArr.length === 0) console.log(-1);
else {
  console.log(sumOdd);
  console.log(Math.min(...oddArr));
}
