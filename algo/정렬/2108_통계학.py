import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())

num_list = [int(input()) for _ in range(n)]
ans=[]
ans.append(round(sum(num_list)/n))
num_list.sort()
ans.append(num_list[n//2])
cnt = Counter(num_list)
most = list(cnt.most_common(2))
# print("most",most)
if most[0][1]==most[1][1]:
    ans.append(most[1][0])
else:
     ans.append(most[0][0])
ans.append(num_list[-1]-num_list[0])

for i in ans:
    print(i)