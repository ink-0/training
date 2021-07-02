# 체육복

[링크](https://programmers.co.kr/learn/courses/30/lessons/42862?language=javascript)

### 📌 내 풀이

1. 전체 학생 수 - 잃어버린 수
2. 자기가 가져온 여벌을 잃어버린 학생수 빼기
3. 남은 잃어버린 학생수를 돌며 +1, -1인경우 더해주기

<br>

### 📌 다른 풀이

```js
function solution(n, lost, reserve) {
  return (
    n -
    lost.filter((lstu) => {
      const spareStu = reserve.find((rstu) => Math.abs(rstu - lstu) <= 1);
      if (!spareStu) return true;
      reserve = reserve.filter((rstu) => rstu !== spareStu);
    }).length
  );
}
```

1. `lost` 를 돌며 filter
2. `reserve`를 돌며 여유학생과 잃은학생의 차이가 1보다 작은 학생의 값을 찾음
3. 그 학생이 없으면 true
4. 그 학생이 있으면 `reserve`에서 빼주며 등장

하지만 이 풀이는 여벌을 챙겼으나 도난당한 학생을 먼저 제거하지 않았기때문에 테스트케이스1개를 놓치게 된다.

<br>

### 느낀점

- `0%3`이 0인 case를 계산하지 못해 오래 걸렸다.
- 지나치게 많은 for문, if 문 어쩌지..?
- 다른 풀이를 보니 별다른 방법이 없었다. 오히려 함수를 사용해서 나눈것이 잘했다고나 할까? 기분이 좋다 ^.^
