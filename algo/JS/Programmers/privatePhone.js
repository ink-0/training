function solution(phone_number) {
  var answer = '';
  var delLen = phone_number.length - 4;
  var answer = phone_number.slice(delLen);

  answer = '*'.repeat(delLen) + answer;
  return answer;
}
