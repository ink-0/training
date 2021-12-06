// var isPalindrome = function (s) {
//   s = s.toUpperCase();
//   let arr = [];
//   for (let i = 0; i < s.length; i++) {
//     if ((s[i] >= 'A' && s[i] <= 'Z') || (s[i] >= '0' && s[i] <= '9')) {
//       arr.push(s[i]);
//     }
//   }
//   return arr.join('') === arr.reverse().join('');
// };

var isPalindrome = function (s) {
  const regExp = /[^\da-zA-Z]/g;
  s = s.toUpperCase().replace(regExp, '');
  for (let i = 0, j = s.length - 1; i <= j; i++, j--) {
    if (s[i] !== s[j]) return false;
  }
  return true;
};
