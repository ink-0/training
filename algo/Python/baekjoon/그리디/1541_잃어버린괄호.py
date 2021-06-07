import sys
import re
from collections import deque

input= sys.stdin.readline


ans=0
problem = input().split('-');
for i in problem[0].split('+'):
    ans+=int(i)

for j in problem[1:]:
    for k in j.split('+'):
        ans-=int(k)

print(ans)