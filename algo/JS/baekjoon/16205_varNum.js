const fs = require('fs');

let [num, varName] = (fs.readFileSync('./test') + '')
  .toString()
  .trim()
  .split(' ');

function solution(num, varName) {
  const len = varName.length;
  let arr = null;

  switch (num) {
    case 2:
      arr = varName.split('_');
      break;
    case 1:
    case 3:
      arr = [];
      for (let i = 0; i < len; i++) {
        if ('A' <= varName[i] && varName[i] <= 'Z') arr.push(i);
      }
      arr.push(varName.length);
      if (num === 3) arr.shift();

      arr = arr?.reduce(
        (a, c) => {
          const x = a.pop();
          a.push(varName.slice(x, c).toLowerCase(), c);
          return a;
        },
        [0]
      );
      arr.pop();
      break;
  }

  let output = '';
  output +=
    arr?.reduce((a, c) => {
      return a + c.slice(0, 1).toUpperCase() + c.slice(1);
    }) + '\n';
  output +=
    arr?.reduce((a, c) => {
      return a + '_' + c;
    }) + '\n';
  output +=
    arr?.reduce((a, c) => {
      return a + c.slice(0, 1).toUpperCase() + c.slice(1);
    }, '') + '\n';

  return output;
}
solution(num, varName);
