import sys
input = sys.stdin.readline

n = int(input())

pro = list(input().strip() for _ in range(n))

def isO(ele,curScore):
    if(ele=="X"):
        return 0
    elif(ele=="O"):
        curScore+=1
        return curScore
ansList=[]
for i in pro:
    ans=0
    cur=0
    for j in i:
        cur=isO(j,cur)
        ans+=cur
    ansList.append(ans)

for i in ansList:
    print(i)