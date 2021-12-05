var climbStairs = function (n) {
  if ((n === 0) | (n === 1)) return 1;

  const DP = new Array(n + 1).fill(0);

  [DP[1], DP[2]] = [1, 2];
  for (let i = 3; i <= n; i++) {
    DP[i] = DP[i - 2] + DP[i - 1];
  }
  return DP[n];
};

console.log(climbStairs(3));
