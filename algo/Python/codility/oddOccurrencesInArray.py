def solution(A):
    if len(A) ==1:
        return A[0]
    A = sorted(A)

    for i in range(0,len(A),2):
        if i+1 == len(A):
            return A[i]
        if A[i]!=A[i+1]:
            return A[i]
# 시간복잡도 
# def solution(A):

#     cntDic={}

#     for i in A:
#         if i not in cntDic:
#             cnt=0
#             for j in A:
#                 if j==i:
#                     cnt+=1
#             cntDic[i]=cnt
#     for num,cnt in cntDic.items():
#         if cnt%2==1:
#             return num