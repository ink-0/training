const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync("./test").toString().trim().split("\n");
let input = (fs.readFileSync('./test') + '')
  .trim()
  .split('\n')
  .map((e) => e.split(' ').map(Number));
input.shift();

const nArr = input.map((arr) => {
  const [num, n] = [arr[0], arr[1]];
  return num.toString(n);
});

const isPalindrome = (num) => {
  let lenNum = num.length;
  let hLenNum = Math.floor(num.length / 2);

  for (let i = 0; i < hLenNum; i++) {
    if (num[i] !== num[lenNum - i - 1]) return 0;
  }
  return 1;
};

nArr.map((n) => console.log(isPalindrome(n)));
