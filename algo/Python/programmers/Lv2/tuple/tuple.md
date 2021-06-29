# 튜플

[링크](https://programmers.co.kr/learn/courses/30/lessons/64065)

### 📌 내 풀이

1. `},`로 나누기
2. `{}`없애고 나누기 각 숫자를 이중배열로 생성
3. 길이순으로 오름차순 후 다음 값과 비교하여 없는 값 답으로

### 📌 다른 풀이1

```py
import re
from collections import Counter
def solution(s):

    s = Counter(re.findall('\d+', s))
    print(s)
    print(s.items())
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

```

```
Counter({'2': 4, '1': 3, '3': 2, '4': 1})
dict_items([('2', 4), ('1', 3), ('3', 2), ('4', 1)])
```

counter를 활용하여 각 숫자의 개수를 구했다.
숫자가 적은 순으로 나열한 다음 처음부터 센다.

### 📌 다른 풀이2

```py
 s1 = s.lstrip('{').rstrip('}').split('},{')
```

파싱을 깔끔하게 구현해낸방법

### 내가 간과한 점

정해진 풀이 방법에만 갇혀서 생각하다 보니 효율적인 풀이법을 생각하지 못했다. 특시 개수를 세는 방식은 생각을 못했다.
