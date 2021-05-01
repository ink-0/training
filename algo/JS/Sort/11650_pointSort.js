const fs = require("fs");
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync("./test").toString().trim().split("\n");
let input = (fs.readFileSync("./test") + "")
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map(Number));
input.shift();
// console.log(input);
// let point_lst = [];
// input.map((ele, i) => {
//   point_lst.push(ele.split(" "));
// });

console.log(
  input
    .sort((a, b) => a[0] - b[0] || a[1] - b[1])
    .join("\n")
    .replace(/\,/g, " ")
);
