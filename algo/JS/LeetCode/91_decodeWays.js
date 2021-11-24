var numDecodings = function (s) {
  const DP = Array(s.length + 1).fill(0);

  if (s[0] === '0') return 0;

  DP[0] = 1;
  DP[1] = 1;

  for (let i = 2; i <= s.length; i++) {
    const oneDigit = +s.slice(i - 1, i);
    const twoDigits = +s.slice(i - 2, i);

    if (oneDigit > 0) DP[i] = DP[i - 1];
    if (twoDigits >= 10 && twoDigits <= 26) DP[i] += DP[i - 2];
  }
  return DP[s.length];
};

numDecodings('1106');
