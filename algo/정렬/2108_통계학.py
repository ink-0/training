import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())

num_list = [int(input()) for _ in range(n)]
ans=[]
# ans.append(round(sum(num_list)/n))
# num_list.sort()
# ans.append(num_list[n//2])
# cnt = Counter(num_list)
# most = list(cnt.most_common(2))
# # print("most",most)
# if n==1:
#     ans.append(most[0][0])
# else:
#     if most[0][1]==most[1][1]:
#         ans.append(most[1][0])
#     else:
#         ans.append(most[0][0])
    
# ans.append(num_list[-1]-num_list[0])

# for i in ans:
#     print(i)
a=[]
q = [0]*8001
for i in num_list:
    q[i+4000]+=1
qmax = max(q)
for i in range(8001):
    if q[i] == qmax:
        a.append(i-4000)

a.sort()
ans.append(round(sum(num_list)/n))
ans.append(sorted(num_list)[n//2])
if len(a)==1:
    ans.append(a[0])
else:
    ans.append(a[1])
ans.append(max(num_list)-min(num_list))
for i in ans:
    print(i)