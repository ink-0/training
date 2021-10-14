const fs = require('fs');
const { isModuleNamespaceObject } = require('util/types');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

input.shift();

let stack = [];

// input.map((cmd) => {
//   const cmdArr = cmd.split(' ');
//   const command = cmdArr[0];

//   switch (command) {
//     case 'push':
//       const number = cmdArr[1];
//       stack.push(parseInt(number));
//       break;
//     case 'top':
//       if (stack.length === 0) console.log(-1);
//       else console.log(stack[stack.length - 1]);

//       break;
//     case 'pop':
//       if (stack.length === 0) console.log(-1);
//       else console.log(stack.pop());
//       break;
//     case 'size':
//       console.log(stack.length);
//       break;
//     case 'empty':
//       if (stack.length === 0) console.log(1);
//       else console.log(0);
//   }
// });

let top = 0;
let ans = '';

const cmdObj = {
  pop: () => stack.pop() || -1,
  size: () => stack.length,
  empty: () => (stack[0] ? 0 : 1),
  top: () => stack[stack.length - 1] || -1,
  push: (item) => {
    stack.push(item.split(' ')[1]);
    return '';
  },
};

const result = input.reduce(
  (acc, v) => acc + (cmdObj[v] ? `${cmdObj[v]()}\n` : cmdObj.push(v)),
  ''
);

console.log(result);
