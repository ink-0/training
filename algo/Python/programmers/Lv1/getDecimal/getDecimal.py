from itertools import combinations
def solution(nums):
    answer = -1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# 소수 : 나 말고 다른 나머지가 없을 때 
    cnt=0
    sumArr=[]
    comArr = list(combinations(nums,3))

    for i in comArr:
        sumArr.append(sum(i))
        
    for i in sumArr:
        for j in range(2,i):

            if i%j==0:
                break
            elif j == i-1:
                cnt+=1
    
            
    return cnt
