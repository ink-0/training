// 풀이1 (82%)
function solution(X, A) {
  ans = -1;
  let idxArr = new Array(X).fill(0);

  const isContinue = (arr) => {
    let ans = true;
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] === 0) {
        ans = false;
        break;
      }
    }
    return ans;
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

// 풀이 2

function solution(X, A) {
  idxArr = new Array(A.length).fill(0);
  idxSum = 0;
  for (let i = 0; i < A.length; i++) {
    if (idxArr[A[i] - 1] === 0) {
      idxArr[A[i] - 1] = 1;
      idxSum += 1;
    }
    if (idxSum === X) return i;
  }
  return -1;
}
