var coinChange = function (coins, amount) {
  let DP = new Array(amount + 1).fill(amount + 1);
  console.log(DP);
  let coinLen = coins.length;

  if (amount < 0) return -1;
  if (amount === 0) return 0;
  DP[0] = 0;

  for (let i = 1; i <= amount; i++) {
    for (let coin of coins) {
      if (i >= coin) {
        DP[i] = Math.min(DP[i], DP[i - coin]) + 1;
        // console.log(DP);
      }
    }
  }

  return DP[amount] > amount ? -1 : DP[amount];
};
