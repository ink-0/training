function solution(n) {
  var answer = 0;
  //   String(n)
  //     .split("")
  //     .map((ele) => (answer += parseInt(ele)));
  //   return answer;
  // return (n + "").split("").reduce((acc, cur) => acc + parseInt(cur), 0);
  return [...(n + "")].reduce((acc, cur) => acc + cur * 1, 0);
}
console.log(solution(123));
