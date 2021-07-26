# def solution ():
#     n,m = map(int,input().split())
#     graph = []
#     for i in range(n):
#         graph.append(list(map(int,input())))

#     def dfs(x,y):
#         #범위 넘은 경우
#         if x<=-1 or y<=-1 or x>=n or y>=m:
#             return False
#         #구멍이 뚫려 있는 경우
#         if graph[x][y] ==0:
#             graph[x][y]=1
#             dfs(x-1,y)
#             dfs(x+1,y)
#             dfs(x,y-1)
#             dfs(x,y+1)
#             return True
#        #구멍이 막혀있는 경우
#         return False
#     ans = 0
#     for i in range(n):
#         for j in range(m):
#             if dfs(i,j)==True:
#                 ans+=1
#     print(ans)

def solution():
    n,m = map(int,input().split())
    graph = []
    cnt=0

    for i in range(n):
        graph.append(list(map(int,input())))
    

    def bfs(x,y):
        if x<0 or y<0 or x>=n or y>=m:
            return False
        if graph[x][y]==0:
            graph[x][y]=1
            bfs(x,y-1)
            bfs(x,y+1)
            bfs(x-1,y)
            bfs(x+1,y)
            return True
        return False
    


    for i in range(n):
        for j in range(m):
            if bfs(i,j):
                cnt+=1
    print(cnt)

solution()

