const { Console } = require('console');
const fs = require('fs');
const input = fs.readFileSync('../../test').toString().trim().split('\n');

let [n, m] = input.shift().split(' ');

console.log(input);
let result = 0;
let min_num = 0;

input.map((el) => {
  arr = el.split(' ').map(Number);
  min_num = Math.min(...arr);
  result = Math.max(result, min_num);
});

// for (let i = 0; i < n; i++) {
//   min_num_arr = input[i].split(' ').map(Number);
//   console.log(Math.min(min_num_arr));
//   result = Math.max(result, min_num);
// }
console.log(result);
