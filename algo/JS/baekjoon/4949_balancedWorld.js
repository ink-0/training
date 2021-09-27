const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('.');

input.pop();
input.pop();

const bracketStack = [];

// 각 괄호가 나올때마다 조건ㅁ문 하기
const ans = input.map((sentence) => {
  sentence.forEach((alpha) => {
    if (word === '(' || word === '[') {
      bracketStack.push(word);
    } else if (word === ')') {
      if (bracketStack.pop() !== '(') return 'no';
    } else if (word === ']') {
      if (bracketStack.pop() !== '[') return 'no';
    }
  });
});
