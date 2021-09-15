function solution(X, Y, D) {
  Y -= X;
  return Math.ceil(Y / D);
}
