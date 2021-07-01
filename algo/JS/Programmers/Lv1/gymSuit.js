function solution(n, lost, reserve) {
  var answer = 0;
  n -= lost.length;
  lost.map((ele) => {
    if (ele in reserve) {
      reserve.splice(reserve.indexOf(ele), 1);
      n += 1;
    } else if (ele - 1 in reserve) {
      reserve.splice(reserve.indexOf(ele), 1);
      n += 1;
    } else if (ele + 1 in reserve) {
      reserve.splice(reserve.indexOf(ele), 1);
      n += 1;
    }
  });
  return n;
}
