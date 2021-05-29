def solution(s):
    answer = ''
    numArr = list(map(int,s.split()))

    answer=str(min(numArr))+" "+str(max(numArr))
    
    return answer