# [카오 블라인드 채용] 다트게임

[링크](https://programmers.co.kr/learn/courses/30/lessons/17682)

### 📌 내 풀이

1. \*: 전,현 2배 #: -1곱하기
2. 숫자이면 다음거 보기
3. 알파벳이 나오면 방금까지 계싼한 걸 배열에 넣음
4. 보너스 점수가 나오면 배열에 들어잇는 값을 꺼내서 해당 계산 해주기
5. 정해진 값은 미리 조건으로 빼주자

`score` 라는 임시변수에 숫자를 넣어두고
그 뒤에 **보너스** 혹은 **알파벣** 이 나올 경우에 값을 계산해 `answer` 배열에 넣었다.

<br>

### 📌 개선 풀이

```py
import re
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
```

**정규표현식**을 이용한 깔끔한 풀이! 감탄했다.  
일단 복잡한 조건식이 없어서 직적으로 이해가 되었다.

`compile` 과 `findall`의 존재를 처음 알게 되었는데  
`compile`: 정규 표현식을 미리 컴파일해서 패턴을 저장해놓고 사용  
`findall`: 패턴 컴파일 없이 바로 적용도 가능

```py
pattern1 = re.compile("\d{2}")
pattern1.findall("dflds78flksd")
# '78'
re.findall("\d{2}","dflds78flksd")
```

<br>

### 느낀점

- 중첩된 if 조건문이 아쉽다
- 정규표현식의 존재를 알고도 활용하지 못하다니..?
