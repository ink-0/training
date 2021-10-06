const fs = require('fs');

let input = fs.readFileSync('./test');

const money = [500, 100, 50, 10, 5, 1];

let left = 1000 - input;

let cnt = 0;
money.forEach((m) => {
  cnt += parseInt(left / m);
  left %= m;
});

console.log(cnt);
