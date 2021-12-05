var numDecodings = function (s) {
  let DP = new Array(s.length + 1).fill(0);
  console.log(DP);

  DP[0] = 0;
  DP[1] = 1;

  // DP[n] = n개 까지의 decode 가능 갯수
  for (let i = 2; i <= s.length; i++) {
    let one = s.slice(i - 1, i);
    let two = s.slice(i - 2, i);

    // 한자리 수가 decode 가능하다면 : 이전거의 비용
    if (one > 0) DP[i] = DP[i - 1];
    // 두자리 수가 decode 가능하다면 : 현재거의 비용 + 이전거의 비용
    if (two >= 10 && two <= 26) DP[i] += DP[i - 1];
    console.log(i, DP);
  }
  return DP[s.length];
};
numDecodings('1106');
