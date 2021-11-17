const fs = require('fs');

let [num, type] = (fs.readFileSync('./test') + '').toString().trim().split(' ');

let ans = [];
ans[Number(num) - 1] = type;

const getCamelCase = (word) => {
    word.map(w => {
        if(word.toUpperCase())
    })
 }
for (let i = 0; i < 3; i++) {
  if (!ans[i]) {
  }
}
