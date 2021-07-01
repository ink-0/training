function solution(N, stages) {
  var answer = [];
  // return answer;
  //stage를 set으로 해서 중복없는 레벨들 배열을 구함
  // stages를 돌며 set의 인자가 잇는 개수를 셈
  // 도달한 플레이어수 : stages 중 >=set인자
  // 도달햇으나 클리어 못한 수: stages 중 == set인자
  // 그 object에 넣음 failARR[setd인자]=실패율
  // 실패율 기준으로 정렬
  // var failObj={};
  var failArr = [];
  for (let i = 1; i <= N; i++) {
    if (stages.includes(i)) {
      var sucessPlayer = 0;
      var failPlayer = 0;

      stages.map((ele, idx) => {
        if (i < ele) {
          sucessPlayer += 1;
        } else if (i == ele) {
          failPlayer += 1;
        }
      });
      failArr.push([i, failPlayer / (sucessPlayer + failPlayer)]);
    } else {
      failArr.push([i, 0]);
    }
  }
  failArr.sort((a, b) => b[1] - a[1]);
  failArr.map((ele) => answer.push(ele[0]));
  return answer;
}

function solution(participant, completion) {
  participant.sort();
  completion.sort();
  console.log(participant, completion);

  for (let i = 0; i <= participant.length; i++) {
    if (participant[i] !== completion[i]) return participant[i];
  }
}
