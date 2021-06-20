# def solution(A):
#     sumArr=[]
#     length=len(A)
#     for i in range(1,len(A)):
#         sumArr.append(abs(sum(A[:i])-sum(A[i:length])))

#     return min(sumArr)

def solution(A):
    firstSum=0
    lastSum=sum(A)
    minSum=None
    for i in range(1,len(A)):
        firstSum +=A[i-1]
        lastSum-=A[i-1]
        diff = abs(firstSum-lastSum)
        if minSum==None:
            minSum = diff
        else:
            minSum = min(minSum,diff)
    return minSum