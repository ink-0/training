from collections import deque
import math

def solution(progresses, speeds):
    leftTask=[]
    day=[]
    ans=[]
    
    for task in progresses:
        leftTask.append(100-task)
        
    for i in range(len(progresses)):
        if leftTask[i]%speeds[i]!=0:
            day.append(leftTask[i]//speeds[i]+1)
        else:
            day.append(leftTask[i]//speeds[i])

    # 한번에 하는 방법
    # for i in range(len(progresses)):
    #     day.append(math.ceil((100-progresses[i])/speeds[i]))
    deqDay = deque(day)

    
    while deqDay:
        deployCnt=0
        beforeTask = deqDay[0]
        
        for i in deqDay:
            if i<=beforeTask:
                deployCnt+=1
            else:
                break

        for _ in range(deployCnt):
            deqDay.popleft()
        ans.append(deployCnt)
    return ans
        