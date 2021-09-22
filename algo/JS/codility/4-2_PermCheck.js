function solution(A) {
  A.sort((a, b) => a - b);

  if (A[0] !== 1) return 0;

  for (let i = 0; i < A.length - 1; i++) {
    if (A[i] + 1 !== A[i + 1]) {
      return 0;
    }
  }
  return 1;
}
a = [];

for (let i = 0; i < 99; i++) {
  a[i] = i + 2;
}
console.log(a);
console.log(solution(a));
