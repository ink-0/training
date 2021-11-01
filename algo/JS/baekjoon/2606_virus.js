const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

const computerCnt = Number(input.shift());
const pair = Number(input.shift());
let graph = [...Array(computerCnt + 1)].map(() => []);
let visited = Array(computerCnt + 1).fill(false);
let ans = 0;

const dfs = (v) => {
  if (visited[v]) {
    return;
  }
  visited[v] = true;
  ans++;
  graph[v].forEach((vertex) => {
    if (!visited[vertex]) {
      dfs(vertex);
    }
  });
};

for (let i = 0; i < computerCnt - 1; i++) {
  let [num1, num2] = input[i].split(' ').map((num) => Number(num));
  graph.push(num1);
  graph.push(num2);
  dfs(1);
}
console.log(ans - 1);
