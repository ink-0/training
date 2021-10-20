const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

let day = parseInt(input.shift());
let carNumArr = input[0].split(' ').map((ele) => parseInt(ele));

let cnt = 0;

carNumArr.map((carNum) => {
  let banDays = [];
  if (carNum !== 0) {
    banDays = [carNum, carNum + 10, carNum + 20];
  } else {
    banDays = [10, 20, 30];
  }

  if (banDays.indexOf(day) >= 0) cnt += 1;
});
console.log(cnt);
