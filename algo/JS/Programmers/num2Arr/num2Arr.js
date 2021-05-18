function solution(n) {
  //   var answer = [];
  //   var nArr = (n + '').split('').map((ele) => parseInt(ele));
  //   var nArrLen = nArr.length;
  //   for (let i = nArrLen - 1; i >= 0; i--) {
  //     answer.push(nArr[i]);
  //   }

  return (n + '')
    .split('')
    .reverse()
    .map((ele) => parseIntI(ele));
  //   return answer;
}
