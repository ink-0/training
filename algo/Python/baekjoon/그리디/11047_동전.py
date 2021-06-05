import sys
input= sys.stdin.readline

coins=[]
coinCnt=0

n,k = map(int,input().split())

for i in range(n):
    coins.append(int(input()))

left=0
for j in range(len(coins),0,-1):
    coinCnt+=k//coins[j-1]
    k=k%coins[j-1]

print(coinCnt)
