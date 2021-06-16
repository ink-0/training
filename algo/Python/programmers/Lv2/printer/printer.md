# 오픈 채팅방

[링크](https://programmers.co.kr/learn/courses/30/lessons/42587)

### 📌 내 풀이

#### 처음생각

스택과 큐의 개념이 정확히 확립되지 않아
딕셔너리 형태로 값과 인덱스를 저장한 후에  
`priorities` 를 돌며 최대값인지 확인하고 제거
뺀 값의 앞뒤 최대값 비교 -> 조건문으로 처리 하려고 했었다.

하지만 너무 비효율적인 방법인 것 같아

1. 인덱스 배열 생성
2. 탐색 위치 변수 생성
3. 최종 순서의 첫번째 올 값부터 차례로 채워주기 (인덱스 배열도 함께 움직임)
4. 내림차순 정렬이 되었을때 종료하고 `location`값 찾기
   이와 같은 방법으로 구현했다.

<br>

### 📌 다른 풀이

```py
from collections  import deque
arr=[1,3,2]
d = deque( [(i,v) for i,v in enumerate(arr)] #[(0,1),(1,3),(2,2)]

while len(d):
	item =d.popleft() # d에서 가장 앞의 값 빼기
	if d and max(d)[0] > item[0] # d가존재하고, 현재 값 < d의 최대값
		d.append(item) # d에서 제거후 다시 끝에 넣어줌 [(1,3),(2,2),(0,1)]
	else:
		answer+=1
		if item[0] == 찾는값:
			break
```

1. `queue`를 만든다
2. 첫번째 값을 저장해놓고 비교

### 📌 다른 풀이2

```py
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    print(queue)
    answer = 0
    while True:
        cur = queue.pop(0)
        print(cur,",",queue)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
```

이렇게 `deque`를 쓰지 않더라도 any를 사용해서  
저 중에 하나가 True이면 돌아가도록 설꼐

#### any : 단하나만 True이면 True

### 내가 관과한 점
