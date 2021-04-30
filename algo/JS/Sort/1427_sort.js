const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

console.log(input);
const numLst = [];

for (let i = 0; i < input.length; i++) {
  numLst.push(input[i]);
}

console.log(
  numLst
    .sort((a, b) => b - a)
    .join("")
    .trim()
);

// const arr = require("fs")
//   .readFileSync("./test")
//   .toString()
//   .trim()
//   .split("")
//   .map((i) => parseInt(i));
// const nums = Array(10).fill(0);
// arr.forEach((i) => (nums[9 - i] += 1));

// console.log(nums);
// let sorted = "";
// for (let i = 0; i < nums.length; i++) {
//   sorted += String(9 - i).repeat(nums[i]);
//   console.log("i=", i);
// }
// console.log(sorted);
