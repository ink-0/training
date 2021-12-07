var validPalindrome = function (s) {
  let cnt = 0;
  const isPalindrome = (s) => s === s.split('').reverse().join('');

  for (let i = 0, j = s.length - 1; i <= j; i++, j--) {
    if (s[i] !== s[j]) {
      if (s[i + 1] !== s[j] && s[j - 1] !== s[i]) return false;
      else if (s[i + 1] === s[j]) {
        cnt += 1;
        i++;
      } else if (s[i] === s[j - 1]) {
        cnt += 1;
        j--;
      }
    }
    if (cnt > 1) return false;
  }
  return true;
};

var validPalindrome = function (s) {
  let cnt = 0;
  const isPalindrome = (s) => s === s.split('').reverse().join('');
  const cut = (s, i) => s.substr(0, i) + s.substr(i + 1);
  for (let i = 0, j = s.length - 1; i <= j; i++, j--) {
    if (s[i] !== s[j]) {
      return isPalindrome(cut(s, i)) || isPalindrome(cut(s, j));
    }
  }
  return true;
};
