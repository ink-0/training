var addStrings = function (num1, num2) {
  const len1 = num1.length;
  const len2 = num2.length;
  const max = Math.max(len1, len2);

  let res = new Array(max);
  let val = 0;
  let carry = 0;

  const rNum1 = num1.split('').reverse();
  const rNum2 = num2.split('').reverse();

  for (let i = 0; i < max; i++) {
    val = Number(rNum1[i] || 0) + Number(rNum2[i] || 0) + carry;
    carry = Math.floor(val / 10);
    res[max - 1 - i] = val % 10;
  }
  return (carry || '') + res.join('');
};
