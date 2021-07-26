from collections import deque

# def solution():
#     n,m = map(int,input().split())

#     graph = []
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     for i in range(n):
#         graph.append(list(map(int,input())))



#     def bfs(x,y):
#         queue = deque()
#         queue.append([x,y])

#         while queue:
#             x,y = queue.popleft()
#             for i in range(4):
#                 nextX,nextY = x+dx[i], y+dy[i]
#                 if nextX<0 or nextY<0 or nextX>=n or nextY>=m:
#                     continue
#                 if graph[nextX][nextY]==0:
#                     continue
#                 if graph[nextX][nextY]==1:
#                     graph[nextX][nextY] = graph[x][y]+1
#                     queue.append([nextX,nextY])
#         return graph[n-1][m-1]
#     print(bfs(0,0))

def solution():
    n,m = map(int,input().split())
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    graph = []
    for i in range(n):
        graph.append(list(map(int,input())))

    def bfs(x,y):
        queue= deque()
        queue.append([x,y])

        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if nx<0 or ny<0 or nx>=n or ny >=m:
                    continue
                if graph[nx][ny]==0:
                    continue
                if graph[nx][ny]==1:
                    graph[nx][ny] = graph[x][y]+1
                    queue.append([nx,ny])
        return graph[n-1][m-1]
    print(bfs(0,0))

    
solution()



