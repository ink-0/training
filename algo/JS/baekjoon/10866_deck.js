const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

input.shift();

let queue = [];

console.log(input);

const cmdObj = {
  push_back: (x) => queue.push(),
  push_front: (x) => queue.unshift(),
  pop_front: () => queue.shift() || -1,
  pop_back: () => queue.pop() || -1,
  size: () => queue.length(),
  empty: () => (queue[0] ? 0 : 1),
  front: () => queue[0],
  back: () => queue[queue.length - 1],
};

const result = input.reduce((acc, v) => {
  if (cmdObj[v]) return `${cmdObj[v]()}\n`;
  else {
  }
});

console.log(result);
