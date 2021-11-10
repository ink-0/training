const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

for (let i = 1; i <= input[0]; i++) {
  let numbers = input[i].split(' ');

  console.log(Number(numbers[0]) + Number(numbers[1]));
}
