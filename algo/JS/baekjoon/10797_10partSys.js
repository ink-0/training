const fs = require('fs');

let [day, carNumArr] = (fs.readFileSync('./test') + '')
  .toString()
  .trim()
  .split('\n');

const ans = carNumArr.split(' ').filter((num) => num === day).length;
console.log(ans);
