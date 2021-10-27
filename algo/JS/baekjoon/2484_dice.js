const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

input.shift();
let ansArr = [];

input.map((diceSet) => {
  let ans = 0;
  const diceDict = {};
  diceArr = diceSet.split(' ').map((d) => Number(d));

  diceArr.map((dice) => {
    if (diceDict[dice]) diceDict[dice] += 1;
    else diceDict[dice] = 1;
  });

  const fKey = Object.keys(diceDict)[0];
  const fValue = diceDict[Object.keys(diceDict)[0]];

  if (fValue === 4) ans += 50000 + fKey * 5000;
  else if (fValue === 3) ans += 10000 + fKey * 1000;
  else if (fValue === 1) {
    ans += Math.max(...Object.keys(diceDict).map((e) => Number(e))) * 100;
  } else if (fValue === 2) {
    const sKey = Object.keys(diceDict)[1];
    const sValue = diceDict[Object.keys(diceDict)[1]];
    if (sValue === 2) {
      ans += 2000 + fKey * 500 + sKey * 500;
    } else ans += 1000 + fKey * 100;
  }
  ansArr.push(ans);
});
console.log(Math.max(...ansArr));
