n = int(input())
money  = list(map(int,input().split()))

# maxM = max(money)

# confirm = [0 for i in range(10000)]
# print(confirm)
# for i in range(len(money)):
#     for j in range(i+1,len(money)):
#         confirm[i+j] = 1

# print(confirm.find(0,1))

for m in money:
    if target<m:
        break
    target += m

pirnt(target)