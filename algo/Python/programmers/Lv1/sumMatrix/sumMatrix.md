# 행렬의 덧셈

## 카카오 블라인드 채용 [링크](https://programmers.co.kr/learn/courses/30/lessons/12950)

### 📌 내 풀이

1. 행과 열에서 각각 for 문
2. 행 for 문을 돌 때마다 []배열 추가

<br>

### 📌 개선 풀이1

배열을 따로 만들지 않고 A의 값을 더해주는 방법

```py
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    return A
```

### 📌 개선 풀이2

한줄로 끝내는 법

```py
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]

```

<br>

### 느낀점

`zip`을 사용해볼 생각을 못했다. 알고리즘에서 중요한건 어떤 함수와 기능을 활용할지 떠올리는 것이다!
