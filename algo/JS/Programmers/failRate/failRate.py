def solution(N, stages):
    answer = []
    failLst = []
    people = len(stages)
    cnt = 0
    
    for i in range (N):
        
        cnt = stages.count(i+1)
        
        if cnt:
            failLst.append([cnt/(people),i+1])
        else:
            failLst.append([0,i+1])
        
        people -= cnt
        cnt = 0
        
    
    for res in sorted(failLst,key = lambda x: (x[0],-x[1]) ,reverse=True):
        answer.append(res[1])
    return answer