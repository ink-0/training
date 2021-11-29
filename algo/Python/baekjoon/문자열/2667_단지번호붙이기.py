import sys
input = sys.stdin.readline

def DFS(r,c):
    global callCnt
    callCnt += 1

    for k in range (4):
        nextRow = r + dr[k]
        nextCol = c + dc[k]

        if (0 <= nextRow < N and 0 <= nextCol < N):
            if visit[nextRow][nextCol] == 0 and houseComplex[nextRow][nextCol] != 0:
                visit[nextRow][nextCol] = 1
                DFS(nextRow,nextCol)

N = int(input())
houseComplex = [list(map(int,input().strip())) for _ in range (N)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]
visit = [ [0]*N for _ in range (N) ]

complexCnt = 0
complexArr = []
for r in range (N):
    for c in range (N):
        if visit[r][c]:
            continue
        if houseComplex[r][c] != 0:
            callCnt = 0
            visit[r][c] = 1
            DFS(r,c)
            complexArr.append(callCnt)
            complexCnt += 1

complexArr = sorted(complexArr)
print(complexCnt)
for i in complexArr:
    print(i)