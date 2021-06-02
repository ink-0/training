import sys
input= sys.stdin.readline
#1000 - 입력값 
# 0이될때까지 큰것부터 차례로 -

charge=1000-int(input())
coinCnt=0
coins=[500,100,50,10,5,1];

for coin in coins:
    coinCnt+=charge//coin
    charge=charge%coin

print(coinCnt)