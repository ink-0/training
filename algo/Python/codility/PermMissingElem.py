# def solution(A):
#     if len(A)==1:
#         return A[0]
#     A=sorted(A)
    
#     for idx in range(1,len(A)+1):

#         if A[idx]-1 != A[idx-1]:
#             return A[idx]-1

def solution(A):
    arr = [0] * (len(A) + 1)
    for i in A:
        arr[i-1] =1
    return arr.index(0)+1