function solution(s) {
  var wordLen = s.length / 2;

  if (Number.isInteger(wordLen)) return s.substr(wordLen - 1, 2);
  else return s[parseInt(wordLen)];
}
