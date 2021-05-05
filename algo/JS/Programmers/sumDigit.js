function solution(n) {
  var answer = 0;
  String(n)
    .split("")
    .map((ele) => (answer += parseInt(ele)));
  return answer;
}
