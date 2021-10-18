const fs = require('fs');

let [n, m] = (fs.readFileSync('./test') + '').toString().trim().split(' ');

let ans = [];
let visit = new Array(parseInt(n)).fill(false);

const back = (d, n, m) => {
  console.log(d, n, m, '****************');
  // m개의 원소까지 찼는지 확인
  if (d === m) {
    console.log(...ans);
    return;
  }
  for (let i = 0; i < n; i++) {
    console.log('i:', i, 'visit:', visit, 'ans:', ans);
    if (!visit[i]) {
      visit[i] = true;
      ans.push(i + 1);

      back(d + 1, n, m);

      ans.pop();
      visit[i] = false;
    }
  }
};

back(0, parseInt(n), parseInt(m));
