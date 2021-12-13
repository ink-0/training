var merge = function (num1, m, num2, n) {
  for (let i = 0; i < num1.length; i++) {
    if (i >= m) {
      num1[i] = num2[i - m];
    }
  }
  return num1.sort((a, b) => a - b);
};
