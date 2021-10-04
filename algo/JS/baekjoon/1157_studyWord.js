const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().toLowerCase();

let inputArr = input.split('');

const alpha = new Array(26).fill(0);

inputArr.forEach((i) => (alpha[i.charCodeAt() - 97] += 1));

const max = Math.max(...alpha);
const index = alpha.indexOf(max);

let isSame = false;

for (let i = 0; i < 26; i++) {
  if (alpha[i] === max && index !== i) {
    isSame = true;
    break;
  }
}
console.log(isSame ? '?' : String.fromCharCode(index + 65));
