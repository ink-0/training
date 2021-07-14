# def solution(A, B, K):
#     cnt=0
#     for i in range(A,B+1):
#         if(i%K==0):
#             cnt+=1
#     return cnt

# def solution(A, B, K):
#     namA =A%K
#     namB =B%K
#     ans=B-A+1-namA-namB
#     ans= ans//K
#     return ans+1

# def solution(A, B, K):
#     if A<=K:
#         A=K
    
#     namA =A%K
#     mocA = A//K
#     namB =B%K
#     mocB = B//K
#     cnt = mocB-mocA
#     if namA==0:
#         cnt+=1
#     return cnt
#     ans=B-A+1-namA-namB
#     ans= ans//K
#     return ans+1

def solution(A, B, K):

    mocA = A//K
    namA =A%K
    mocB = B//K
    cnt = mocB-mocA

    if namA==0:
        cnt+=1
        
    return cnt