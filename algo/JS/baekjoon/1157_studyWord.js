const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim();

let inputArr = input.split('');

let ans = {};
inputArr.forEach((i) => {
  let ui = i.toUpperCase();
  if (ans[ui]) ans[ui] += 1;
  else ans[ui] = 1;
});

let a = Object.keys(ans).sort((a, b) => {
  return ans[b] - ans[a];
});

if (ans[a[0]] === ans[a[1]]) console.log('?');
else console.log(a[0]);
