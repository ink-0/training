const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

input.shift();

let queue = [];

const cmdObj = {
  push_back: (x) => {
    queue.push(x);
    return '';
  },
  push_front: (x) => {
    queue.unshift(x);
    return '';
  },
  pop_front: () => queue.shift() || -1,
  pop_back: () => queue.pop() || -1,
  size: () => queue.length,
  empty: () => (queue[0] ? 0 : 1),
  front: () => queue[0] || -1,
  back: () => queue[queue.length - 1] || -1,
};

const result = input.reduce(
  (acc, v) =>
    acc +
    (cmdObj[v]
      ? `${cmdObj[v]()}\n`
      : v.split(' ')[0] === 'push_back'
      ? cmdObj.push_back(v.split(' ')[1])
      : cmdObj.push_front(v.split(' ')[1])),
  ''
);

console.log(result);
