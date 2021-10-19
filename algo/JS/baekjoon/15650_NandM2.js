const fs = require('fs');

let [n, m] = (fs.readFileSync('./test') + '').toString().trim().split(' ');

let visit = new Array(parseInt(n)).fill(false);
n = parseInt(n);
m = parseInt(m);

let ans = [];

const back = (d, n, m, idx) => {
  if (d === m) {
    console.log(...ans);
    return;
  }

  for (let i = idx; i < n; i++) {
    // console.log('i:', i, 'visit:', visit, 'ans:', ans);

    if (visit[i]) continue;
    visit[i] = true;
    ans.push(i + 1);
    back(d + 1, n, m, i);
    ans.pop();
    visit[i] = false;
  }
};
let result = '';

function dfs(d, idx) {
  if (d === m) {
    console.log(...ans);
    return;
  }

  for (let i = idx; i < n; i++) {
    if (visit[i]) continue;
    visit[i] = true;
    ans.push(i + 1);
    dfs(d + 1, i);
    ans.pop();
    visit[i] = false;
  }
}
dfs(0, 0);

back(0, parseInt(n), parseInt(m), 0);
