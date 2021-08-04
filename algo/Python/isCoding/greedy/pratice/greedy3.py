# def solution():
#     n,k = map(int,input().split())
#     cnt=0
#     # while n!=1:
#     #     if n%k ==0:
#     #         n = n/k
#     #         cnt+=1
#     #     else:
#     #         n-=1
#     #         cnt+=1
#     # print(cnt)

#     while n >=k :
#         while n%k!=0:
#             n-=1
#             cnt+=1
#         n//=k
#         cnt+=1
#     while n>1:
#         n-=1
#         cnt+=1
#     print(cnt)

def solution ():
    n = int(input())
    arr = input().split();
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    x,y =1,1
    direction = ['L','R','U','D']
    for a in arr:
        for i in range(len(direction)):
            if a == direction[i]:
                nx = x+dx[i]
                ny = y+dy[i]
        if nx <1 or nx>n or ny<1 or ny>n:
            continue
        x,y = nx,ny
    print(x,y)
solution()
