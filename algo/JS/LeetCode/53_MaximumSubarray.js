var maxSubArray = function (nums) {
  const numLen = nums.length;
  let DP = new Array(numLen).fill(0);

  DP[0] = nums[0];

  for (let i = 1; i < numLen; i++) {
    DP[i] = Math.max(DP[i - 1] + nums[i], nums[i]);
  }
  return Math.max(...DP);
};
