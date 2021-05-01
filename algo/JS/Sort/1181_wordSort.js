const fs = require("fs");
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const input = fs.readFileSync("./test").toString().trim().split("\n");
input.shift();

sorted_lst = new Set(input);
sorted_lst = [...sorted_lst];

// sorted_lst = sorted_lst.sort((a, b) => a.length - b.length || (a > b ? 1 : -1));
// sorted_lst = sorted_lst.sort(function (a, b) {
//   if (a.length > b.length) return 1;
//   if (a.length < b.length) return -1;
//   if (a > b) return 1;
//   if (a < b) return -1;
//   return 0;
// });

console.log(
  [...new Set(input)]
    .sort((a, b) => a.length - b.length || a.localeCompare(b))
    .join("\n")
);
console.log(sorted_lst.join("\n"));
// sorted_lst.map((ele) => console.log(ele));
