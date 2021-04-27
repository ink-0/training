const fs = require("fs");
// const input = fs.readFileSync('/dev/stdin').toString();
const input = fs.readFileSync("./test").toString().split(" ");

var num1 = parseInt(input[0]);
var num2 = parseInt(input[1]);

console.log(num1 + num2);
console.log(num1 - num2);
console.log(num1 * num2);
console.log(Math.floor(num1 / num2));
console.log(num1 % num2);
