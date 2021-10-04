const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');
input.shift();

Arr = input[0].split('');

console.log(Arr.reduce((acc, cur) => parseInt(acc) + parseInt(cur)));
