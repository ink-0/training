function solution(N, A) {
  let ans = new Array(N).fill(0);
  A.forEach((a) => {
    if (a <= N) {
      ans[a - 1] += 1;
    }
  });

  return ans;
}
function solution(N, A) {
  const counter = new Array(N).fill(0);
  let maxCounter = 0;

  A.forEach((item) => {
    let idx = item - 1;
    if (item <= N) {
      counter[idx] += 1;
      maxCounter = Math.max(maxCounter, counter[idx]);
    } else counter.fill(maxCounter);
  });

  return counter;
}
