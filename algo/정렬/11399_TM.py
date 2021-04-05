
import sys
input = sys.stdin.readline

n = int(input())
time = sorted(list(map(int, input().split())))
ans=0
sumans=0
for i in time:
    ans+=i
    sumans+=ans

print(sumans)