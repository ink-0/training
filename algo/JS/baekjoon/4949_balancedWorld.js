const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');
const open = ['(', '['];
const close = [')', ']'];
let bracketStack;
const ans = [];
// 각 괄호가 나올때마다 조건ㅁ문 하기
input.pop();
input.forEach((sentence) => {
  let isBool = false;
  bracketStack = [];

  for (let i = 0; i < sentence.length; i++) {
    if (open.includes(sentence[i])) bracketStack.push(sentence[i]);
    else if (close.includes(sentence[i])) {
      if (bracketStack.pop() !== open[close.indexOf(sentence[i])]) {
        ans.push('no');
        isBool = true;
        break;
      }
    }
  }
  if (!isBool) {
    if (bracketStack.length === 0) ans.push('yes');
    else ans.push('no');
  }
});

console.log(ans.join('\n'));

// const ans = input.map((sentence) => {
//   const bracketStack = [];
//   sentence.split('').forEach((word) => {
//     if (word === '(' || word === '[') {
//       bracketStack.push(word);
//     } else if (word === ')') {
//       if (bracketStack[bracketStack.length - 1] !== '(') return 'no';
//       else bracketStack.pop();
//     } else if (word === ']') {
//       if (bracketStack[bracketStack.length - 1] !== '[') return 'no';
//       else bracketStack.pop();
//     }
//   });

//   if (bracketStack.length !== 0) return 'no';
//   return 'yes';
// });
// ans.forEach((a) => console.log(a));
