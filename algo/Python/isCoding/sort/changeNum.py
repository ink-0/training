# A의 가장 작은 수와 B의 가장 큰수를 바꿔야 한다
# 그때마다 min을 하면 ? -> n + n 

# def solution():
#     n,k = map(int,input().split())
#     A = list(map(int,input().split()))
#     B = list(map(int,input().split()))

#     for i in range(k):
#         minA = min(A)
#         maxB = max(B)
#         A[A.index(minA)],B[B.index(maxB)]=B[B.index(maxB)],A[A.index(minA)]
#     print(A)
#     print(sum(A))
# solution()
def solution ():
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort(reverse=True)

    for i in range(k):
        if A[i]<B[i]:
            A[i],B[i]=B[i],A[i]
        else:
            break
    print(sum(A))
solution()