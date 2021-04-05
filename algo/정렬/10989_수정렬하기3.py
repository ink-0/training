import sys
input = sys.stdin.readline

arr=[0]*10001
n=int(input())

for i in range(n):
    arr[int(input())]+=1


for i in range(0,10001):
    if arr[i]!=0:
        for j in range(arr[i]):
            print(str(i))

