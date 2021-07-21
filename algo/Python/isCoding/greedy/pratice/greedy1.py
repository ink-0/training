# def solution():
#     n,m,k = map(int,input().split())
#     arr = list(map(int,input().split()))
#     arr.sort(reverse=True)
#     print(arr)
#     kCnt=0
#     ans=0
#     if arr[0] ==arr[1]:
#         print(arr[0]*m)
#     else:
#         for i in range(m):
#             if kCnt>=k:
#                 print(i,'큰',ans,'k',kCnt)
#                 ans+=arr[1]
#                 kCnt=0
#             else:
#                 print(i,'작은',ans,'k',kCnt)
#                 ans+=arr[0]
#                 kCnt+=1
#     print(ans)

def solution():
    n,m,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()

    first = arr[n-1]
    second = arr[n-2]

    count = int(m/(k+1))*k
    count += m%(k+1)

    ans=0

    ans += count * first
    ans+= (m-count)*second
    print(ans)

solution()