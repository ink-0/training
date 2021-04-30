const fs = require("fs");
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const input = fs.readFileSync("./test").toString().trim().split("\n");

n = input.shift();
// console.log(input);
let numLst = [];
input.map((ele, i) => {
  numLst.push(ele.split(" "));
});

numLst = numLst.sort(function (a, b) {
  if (parseInt(a[1]) > parseInt(b[1])) return 1;
  if (parseInt(a[1]) < parseInt(b[1])) return -1;
  if (parseInt(a[0]) > parseInt(b[0])) return 1;
  if (parseInt(a[0]) < parseInt(b[0])) return -1;
  return 0;
});

let endTime = 0;
let cnt = 0;
for (let i = 0; i < numLst.length; i++) {
  if (endTime <= parseInt(numLst[i][0])) {
    cnt += 1;
    endTime = parseInt(numLst[i][1]);
  }
}
console.log(cnt);
