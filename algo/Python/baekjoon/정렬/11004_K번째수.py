import sys
input = sys.stdin.readline;

n,k = map(int,input().split())
# arr = [0]*5000000

# for i in range(n):
#     arr[int(input)]=1
num = list(map(int,input().split()))
num.sort()

print(num[k-1])
