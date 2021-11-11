const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');
console.log(input);

const [N, M, V] = input.shift();
let graph = [...Array(N + 1)].map(() => []);
let visited = [...Array(N + 1)].fill(false);
let result = [];

input.forEach((str) => {
  let [v1, v2] = str.split(' ');
  insertEdge(v1, v2);
  insertEdge(v2, v1);
});

dfs(V);
console.log(result.join(' '));

visited.fill(false);
result = [];
bfs(V);
console.log(result.join(' '));

const insertEdge = (start, dest) => {
  for (let i = 0; i < graph[start].length; i++) {
    if (graph[start][i] < dest) continue;
    if (graph[start][i] === dest) i = null;
    break;
  }

  if (i !== null) {
    graph[start].splice(i, 0, dest);
  }
};

const dfs = (v) => {
  if (visited[v]) return;

  visited[v] = true;
  result.push(v);

  graph[v].forEach((vertex) => {
    if (!visited[vertex]) {
      dfs(vertex);
    }
  });
};

const bfs = (vStart) => {
  const willVisit = [vStart];
  let v;
  while (willVisit.length !== 0) {
    v = willVisit.shift();
    if (visited[v]) {
      continue;
    }

    visited[v] = true;
    result.push(v);
    graph[v].forEach((vertex) => {
      if (!visited[vertex]) {
        willVisit.push(vertex);
      }
    });
  }
};
