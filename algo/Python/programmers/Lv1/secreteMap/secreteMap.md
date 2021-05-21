# 1차 비밀지도

## 카카오 블라인드 채용 [링크](https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3)

### 📌 내 풀이

1. 각 숫자 이진수로 변경
2. n의 길이가 안될때 자릿수 맞추기
3. 두 수 비교하며 or 로 "#" " "

풀이 과정에서 길이를 체크하는 함수를 하나 더 만들었고,
`for문`의 개수를 최소화 하려 했지만 이중 for문이 되었다.

<br>

### 📌 개선 풀이

```py
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
```

나는  
`1째 for문` : 2진수로 바꾸기  
`2째 함수` : n개로 맞추기  
`3째 for문` + if 문 : 두 수를 더해서 판별 으로 실행한 동작이

for문 하나에서 해결되면서 효율성이 매우 높아졌다.
`rjust`라는 오른쪽 정렬하는 함수를 알게 되었다.
<br>

### 느낀점

파이썬으로 다양하고 많은 문제를 풀면서 이런 함수들을 적재적소에 구현할 수 있게 될거다.
