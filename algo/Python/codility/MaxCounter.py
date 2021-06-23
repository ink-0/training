# def solution(N, A):

#     ans=[0]*N
#     for num in A:
#         if 1<= num <=N:
#             ans[num-1]+=1

#         else :
#             maxNum = max(ans)
#             ans=[maxNum]*N

#     return ans

def solution(N, A):
    counters = N * [0]
    nextMax =  maxNum = 0

    for i in A:
        if i <= N:
            curr = counters[i-1] = max(counters[i-1] +1, maxNum+1)
            nextMax = max(curr,nextMax)
        else:
            maxNum =nextMax
 

    return [c if c > maxNum else maxNum for c in counters]
