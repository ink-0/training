# 오픈 채팅방

[링크](https://programmers.co.kr/learn/courses/30/lessons/42888)

### 📌 내 풀이

`idNickLst` : id를 key로 객체 존재 ex { uid1234 : Muzi}
`enterLeaveLst` : 입퇴장 리스트

1. Enter : `idNickLst`에 추가 , 입장퇴장리스트에 추가
2. Change: `idNickLst`에 추가
3. Leave : 입장 퇴장리스트에 추가
4. 조건문으로 print record로 print

<br>

### 📌 다른 풀이

```py
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer

```

### 내가 관과한 점

- 공백으로 구분된 입력을 리스트로 만드는 과정에 `map`은 필요없다

```py
        k=list(map(str,r.split()))

        k= r.split()
```

- 프린트를 위한 불필요한 배열,객체를 만들었다.

그래도 split한 배열을 지정해놓고 사용한 건 좋은 것 같다.
