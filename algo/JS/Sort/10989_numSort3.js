const fs = require("fs");
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const input = fs.readFileSync("./test").toString().trim().split("\n");

n = parseInt(input.shift());

numLst = Array(n).fill(0);

input.map((ele, i) => (numLst[ele] += 1));

numLst.map((ele, i) => {
  if (ele !== 0) {
    for (let j = 0; j < ele; j++) {
      console.log(i);
    }
  }
});
// for (let i = 0; i < numLst.length; i++) {
//   if (numLst[i] !== 0) {
//     console.log(input[i]) * i;
//   }
// }
