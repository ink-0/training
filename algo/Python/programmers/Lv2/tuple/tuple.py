import re
def solution(s):
    ans = []
    splitS= s.split('},')

    numArr=[]
    for i in splitS:
        i=re.sub('[{}]','',i)
        numArr.append(i.split(','))

        
    numArr = sorted(numArr, key = lambda x: len(x))
    ans.append(int(numArr[0][0]))
    for i in range(len(numArr)-1):
        for j in numArr[i+1]:
            if j not in numArr[i]:
                ans.append(int(j))
    return (ans)
