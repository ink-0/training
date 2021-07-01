function solution(array, commands) {
  var ans = [];

  ans = commands.map((v) => {
    return array.slice(v[0] - 1, v[1]).sort((a, b) => a - b)[v[2] - 1];
  });

  return ans;
}
