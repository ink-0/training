function solution(numbers, target) {
  return dfs(-1, numbers, target);
  function dfs(idx, numbers, target) {
    //조건을 만족하는 경우
    if (idx === numbers.length - 1) {
      if (target === 0) {
        return 1;
      } else return 0;
    }
    //조건을 만족하지 않는 경우
    else {
      return (
        dfs(idx + 1, numbers, target - numbers[idx + 1]) +
        dfs(idx + 1, numbers, target + numbers[idx + 1])
      );
    }
  }
}
//bfs 시간초과
function solution(numbers, target) {
  let queue = [];
  let cnt = 0;
  queue.push([numbers[0], 0]);
  queue.push([-numbers[0], 0]);

  while (queue.length != 0) {
    let [value, idx] = queue.shift();
    if (idx === numbers.length - 1) {
      if (value === target) {
        cnt += 1;
      }
    } else {
      queue.push([value + numbers[idx + 1], idx + 1]);
      queue.push([value - numbers[idx + 1], idx + 1]);
    }
  }
  return cnt;
}
