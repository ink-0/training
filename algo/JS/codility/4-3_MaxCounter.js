// function solution(N, A) {
//   let ans = new Array(N).fill(0);
//   A.forEach((a) => {
//     if (a <= N) {
//       ans[a - 1] += 1;
//     }
//   });

//   return ans;
// }

function solution(N, A) {
  // write your code in JavaScript (Node.js 8.9.4)
  let ans = new Array(N).fill(0);
  let maxNum = 0;

  A.forEach((a) => {
    let idx = a - 1;
    if (a <= N) {
      ans[idx] += 1;
      maxNum = Math.max(maxNum, ans[idx]);
    } else ans.fill(maxNum);
  });

  return ans;
}
