const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');
const open = ['(', '['];
const close = [')', ']'];

const bool = [];
// 각 괄호가 나올때마다 조건ㅁ문 하기
console.log('인풋', input);
console.log('배열', input.slice(0, input.length - 1));
const ans = input.map((sentence) => {
  const bracketStack = [];
  sentence.split('').forEach((word) => {
    if (word === '(' || word === '[') {
      bracketStack.push(word);
    } else if (word === ')') {
      if (bracketStack[bracketStack.length - 1] !== '(') return 'no';
      else bracketStack.pop();
    } else if (word === ']') {
      if (bracketStack[bracketStack.length - 1] !== '[') return 'no';
      else bracketStack.pop();
    }
  });

  if (bracketStack.length !== 0) return 'no';
  return 'yes';
});
ans.forEach((a) => console.log(a));
