import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int,input().split())) for i in range (n)]
points.sort(key= lambda x: (x[0],x[1]))
for i in points:
    print(*i)