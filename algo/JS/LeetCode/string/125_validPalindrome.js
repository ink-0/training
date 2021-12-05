var isPalindrome = function (s) {
  s = s.toUpperCase();
  let arr = [];
  for (let i = 0; i < s.length; i++) {
    if ((s[i] >= 'A' && s[i] <= 'Z') || (s[i] >= '0' && s[i] <= '9')) {
      arr.push(s[i]);
    }
  }
  return arr.join('') === arr.reverse().join('');
};
