function solution(a, b) {
  let ans = 0;
  a.map((ele, idx) => {
    ans += ele * b[idx];
  });
  //   ans = a.reduce((acc,cur,idx)=> acc+=cur*b[idx],0)

  return ans;
}
