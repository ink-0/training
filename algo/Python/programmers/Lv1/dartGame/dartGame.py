def solution(dartResult):
    answer=[]
    score=0
    dartResult = list(dartResult)
    for idx,dart in enumerate(dartResult):

        if dart == 'S':
            answer.append(score)
        elif dart == 'D':
            answer.append(score*score)
        elif dart == 'T':
            answer.append(score*score*score)
        elif dart == '*':
            curLoc=len(answer)-1
            if curLoc==0:
                answer[curLoc]=answer[curLoc]*2
            else:
                answer[curLoc]=answer[curLoc]*2
                answer[curLoc-1]=answer[curLoc-1]*2
        elif dart == '#':
            curLoc=len(answer)-1
            answer[curLoc]=answer[curLoc]*(-1)
        else:
            if dart=='1':
                if(dartResult[idx+1]=='0'):
                    del dartResult[idx+1]
                    score = 10
                else:
                    score = int(dart)
            
            else: 
                score=int(dart)
            
    return sum(answer)