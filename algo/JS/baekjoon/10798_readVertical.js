const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync("./test").toString().trim().split("\n");
let input = (fs.readFileSync('./test') + '').trim().split('\n');

input.shift();

console.log(input);
