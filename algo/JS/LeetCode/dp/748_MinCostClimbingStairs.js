var minCostClimbingStairs = function (cost) {
  const goalStair = cost.length;
  let DP = [];
  DP[0] = 0;
  DP[1] = 0;
  DP[2] = Math.min(cost[0], cost[1]);

  for (let i = 3; i <= goalStair; i++) {
    let one = DP[i - 2] + cost[i - 2];
    let two = DP[i - 1] + cost[i - 1];
    DP[i] = Math.min(one, two);
    console.log(i, DP);
  }

  return DP[goalStair];
};
