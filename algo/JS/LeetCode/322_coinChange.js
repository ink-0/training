var coinChange = function (coins, amount) {
  let DP = new Array(amount + 1).fill(amount + 1);

  let coinLen = coins.length;

  if (amount < 0) return -1;
  if (amount === 0) return 0;
  DP[0] = 0;

  for (let i = 1; i <= amount; i++) {
    for (let j = 0; j < coins.length; j++) {
      if (i >= coins[j]) {
        DP[i] = Math.min(DP[i], DP[i - coins[j]] + 1);
      }
    }
  }

  return DP[amount] > amount ? -1 : DP[amount];
};
