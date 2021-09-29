const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('');
let ans = new Array(26).fill(0);
input.map((alpha) => {
  let alpha2Ascii = alpha.charCodeAt(0);
  ans[alpha2Ascii - 97] += 1;
});
console.log(ans.join(' '));
