const fs = require("fs");
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const input = fs.readFileSync("./test").toString().split("\n");

const n = input.shift();

console.log(
  input
    .sort((a, b) => a - b)
    .join("\n")
    .trim()
);
