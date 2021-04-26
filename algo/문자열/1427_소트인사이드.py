import sys
input = sys.stdin.readline

numLst=[]
num = input().strip()


for i in num:
    numLst.append(i)

numLst=sorted(numLst,reverse=True)

numLst = "".join(numLst)
print(numLst)