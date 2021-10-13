const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

const n = parseInt(input.shift());

let cnt = 0;
for (let i = 0; i < n; i++) {
  let wordStack = [];
  const word = input[i];

  wordStack.push(word[0]);

  for (let j = 1; j < word.length; j++) {
    const aOrb = word[j];

    if (aOrb === wordStack[wordStack.length - 1]) wordStack.pop();
    else wordStack.push(aOrb);
  }
  if (wordStack.length === 0) cnt++;
}
console.log(cnt);
