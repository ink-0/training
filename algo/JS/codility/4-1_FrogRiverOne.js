function solution(X, A) {
  ans = -1;
  let idxArr = new Array(X).fill(0);

  const isContinue = (arr) => {
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] === 1) return false;
      return true;
    }
  };

  for (let i = 0; i <= A.length; i++) {
    idxArr[A[i] - 1] = 1;
    if (isContinue(idxArr)) {
      ans = i;
      break;
    }
  }

  return ans;
}
