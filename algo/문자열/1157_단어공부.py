import sys
input = sys.stdin.readline

word = input().strip().upper()
cntList=[]
setList = list(set(word))


for i in setList:
    cntList.append(word.count(i))
if(cntList.count(max(cntList))>1):
    print("?")
else:
    print(setList[cntList.index(max(cntList))])

