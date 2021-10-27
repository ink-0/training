const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

input.shift();
let ansArr = [];

// input.map((diceSet) => {
//   let ans = 0;
//   const diceDict = {};
//   diceArr = diceSet.split(' ').map((d) => Number(d));
//   diceArr.sort((a, b) => b - a);

//   diceArr.map((dice) => {
//     if (diceDict[dice]) diceDict[dice] += 1;
//     else diceDict[dice] = 1;
//   });

//   const fKey = Object.keys(diceDict)[0];
//   const fValue = diceDict[Object.keys(diceDict)[0]];

//   if (fValue === 4) ans += 50000 + fKey * 5000;
//   else if (fValue === 3) ans += 10000 + fKey * 1000;
//   else if (fValue === 1) {
//     ans += Math.max(...Object.keys(diceDict).map((e) => Number(e))) * 100;
//   } else if (fValue === 2) {
//     const sKey = Object.keys(diceDict)[1];
//     const sValue = diceDict[Object.keys(diceDict)[1]];
//     if (sValue === 2) {
//       ans += 2000 + fKey * 500 + sKey * 500;
//     } else ans += 1000 + fKey * 100;
//   }
//   ansArr.push(ans);
// });
// console.log(Math.max(...ansArr));
let max = 0;
input.map((diceSet) => {
  let ans = 0;

  diceArr = diceSet.split(' ').map((d) => Number(d));
  diceArr.sort((a, b) => b - a);

  if (diceArr[0] === diceArr[3]) {
    ans = 50000 + diceArr[0] * 5000;
  } else if (diceArr[0] === diceArr[2] || diceArr[1] === diceArr[3]) {
    ans = 10000 + diceArr[1] * 1000;
  } else if (diceArr[0] === diceArr[1] && diceArr[2] === diceArr[3]) {
    ans = 2000 + diceArr[0] * 500 + diceArr[2] * 500;
  } else if (diceArr[0] === diceArr[1]) {
    ans = 1000 + diceArr[0] * 100;
  } else if (diceArr[1] === diceArr[2]) {
    ans = 1000 + diceArr[1] * 100;
  } else if (diceArr[2] === diceArr[3]) {
    ans = 1000 + diceArr[2] * 100;
  } else {
    ans = diceArr[0] * 100;
  }

  max = Math.max(max, ans);
});
console.log(max);
