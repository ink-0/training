# 타겟 넘버

[링크](https://programmers.co.kr/learn/courses/30/lessons/43165)

### 📌 내 풀이

1. `len(numbers)`개수까지의 모든 조합을 구한다
2. 각 수를 더해보고 targets 와 비교하여 cnt 한다.  
   결론적으로 조합을 일일히 계산하는 방법을 알아내지 못했고 라이브러리 사용방법을 찾아 보았다.

<br>

### 📌 다른 풀이

#### 조합만 이용한 경우

```py
from itertools import product
def solution(numbers, target):
    l=[(x,-x) for x in numbers]
    s=list(map(sum,product(*l)))
    return s.count(target)
```

`l= [(1, -1), (1, -1), (1, -1), (1, -1), (1, -1)]`
numbers의 +,- 조합으로 나눠준 후  
s로 모든 경우의 수를 구해 => 더한 값으로 이뤄진 배열을 만든다

### DFS 인 경우

```py
def solution(numbers,target):
    return DFS(-1,numbers,target)

def DFS(idx, numbers, target):
    if idx == len(numbers)-1:
        if target== 0:
            return 1
        else:
            return 0
    else:
        return DFS(idx+1,numbers,target-numbers[idx+1])+DFS(idx+1,numbers,target+numbers[idx+1])
```

`target`값을 1씩 더하고 빼주는 과정을 재귀를 통해 진행한다 .
`target==0`의 의미는 numbers가 여러 조합을 통해 3이 되었다는 뜻이므로 그 경우를 더해주어 최종적으로 target이 나온 수를 알아낸다.

### BFS 인 경우

```py
def bfs(numbers, target):
    queue = []
    cnt = 0
    queue.append([numbers[0],0])
    queue.append([-numbers[0],0])

    while queue:
        print(queue)
        value, idx = queue.pop(0)

        if idx == len(numbers)-1:
            if value == target:
                cnt += 1
        else:
            queue.append([value+numbers[idx+1],idx+1])
            queue.append([value-numbers[idx+1],idx+1])
    return cnt

numbers=[1,1,1,1,1]
target = 3

print(bfs(numbers,target))
```

처음 numbers의 첫번째 값을 `queue`에 넣어 시작  
`queue` : ([numbers의 값, idx])로 이루어져 있음  
`queue` idx가 len(numbers)가 되기 전까지 하나씩 꺼내서 연산 시행한다.
