var minPathSum = function (grid) {
  let mLen = grid.length;
  let nLen = grid[0].length;

  const DP = [...new Array(mLen)].map(() => []);

  DP[0][0] = grid[0][0];

  for (let i = 0; i < mLen; i++) {
    for (let j = 0; j < nLen; j++) {
      if (i === 0 && j === 0) DP[i][j] = grid[i][j];
      // 우측 방향
      else if (j === 0) DP[i][j] = grid[i][j] + DP[i - 1][j];
      // 하단 방향
      else if (i === 0) DP[i][j] = grid[i][j] + DP[i][j - 1];
      // 대각선 방향
      else {
        DP[i][j] = grid[i][j] + Math.min(DP[i][j - 1], DP[i - 1][j]);
      }
    }
  }
  return DP[mLen - 1][nLen - 1];
};
