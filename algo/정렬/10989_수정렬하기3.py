import sys
input = sys.stdin.readline

arr=[0]*10001
n=int(input())
for i in range(n):
    arr[int(input())]+=1;
for i in range(len(arr)):
    if(arr[i]!=0):
        for k in range(arr[i]):
            print(i)
