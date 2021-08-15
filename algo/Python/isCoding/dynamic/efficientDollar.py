n,m = map(int,input().split())
d = [10001] * (m+1)
arr=[]

for i in range(n):
    arr.append(int(input()))

# n 2 m 15
# 2 3
for i in range(n):
    for j in range(arr[i],m+1):
        if d[j-arr[i]]!=10001:
            d[j] = min(d[j],d[j-arr[i]]+1)
            print('j',j,'d[j]',d[j])
if d[m]== 10001:
    print(-1)
else:
    print(d[m])
