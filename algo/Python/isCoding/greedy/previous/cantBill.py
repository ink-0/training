n = int(input())
money  = list(map(int,input().split()))

money.sort()
target = 1

for m in money:
    if target<m:
        break
    target += m

print(target)