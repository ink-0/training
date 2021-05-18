# 프로그래머스 Lv.1 자연수 뒤집어 배열 만들기

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/12932)

### 📌 내 풀이

```js
function solution(n) {
  var answer = [];
  var nArr = (n + '').split('').map((ele) => parseInt(ele));
  var nArrLen = nArr.length;
  for (let i = nArrLen - 1; i >= 0; i--) {
    answer.push(nArr[i]);
  }
  return answer;
}
```

#### 풀이 방법

1. 자연수로 받은 n -> 문자로변경 -> []배열로생성 -> 정수로 바꿈
2. for문을 거꾸로 돌며 answer에 채워줌  


<br>

### 📌 개선 풀이

```js
return (n + '')
  .split('')
  .reverse()
  .map((ele) => parseIntI(ele));
```

`reverse()` 사용으로 한번에 가능

<br>

### 📌 다른 풀이

```js
do {
  arr.push(n % 10);
  n = Math.floor(n / 10);
} while (n > 0);

return arr;
```

수학적으로 접근 가능

<br>

### 느낀점

javascript 의 reverse를 알게 되었고, 또 코드의 효율성을 위해선 다양한 방법으로 고민해봐야 하는 필요성을 느낌
