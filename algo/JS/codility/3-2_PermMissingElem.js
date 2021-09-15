function solution(A) {
  if (A.length === 0) return 1;
  A.sort();

  for (let i = 0; i < A.length; i++) {
    if (A[i] !== i + 1) {
      return i + 1;
    }
  }
  return A.length + 1;
}

function solution(A) {
  if (A.length === 0) {
    return 1;
  }
  return (
    ((A.length + 2) * (A.length + 1)) / 2 -
    A.reduce((accumulator, currentvalue) => accumulator + currentvalue)
  );
}
