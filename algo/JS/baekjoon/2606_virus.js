const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');
let n = Number(input.shift());
let m = Number(input.shift());
let graph = [...new Array(n + 1)].map(() => []);
// let graph2 = new Array(n + 1).fill([]);
let visited = new Array(n + 1).fill(false);
let ans = 0;

visited[1] = true;

const dfs = (start) => {
  graph[start].map((dest) => {
    if (!visited[dest]) {
      visited[dest] = true;
      ans += 1;
      dfs(dest);
    }
  });
};

input.map((i) => {
  const [start, dest] = i.split(' ').map((ele) => Number(ele));
  graph[start].push(dest);
  graph[dest].push(start);
});

dfs(1);

console.log(ans);
