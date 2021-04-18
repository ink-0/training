import sys
input = sys.stdin.readline
sum=0

n = int(input())
aArr = list(map(int,input().split()))
bArr = list(map(int,input().split()))
aArr.sort()
for i in aArr:
    bMax = max(bArr)
    sum+=i*max(bArr)
    bArr.remove(bMax)
    print(i,bArr)

print("합",sum)