n= int(input())


def isVps(word):
    stackLst=[]

    for i in word:
        if i=="(":
            stackLst.append("(")
        else:
            if len(stackLst)==0:
                return "NO"
            stackLst.pop()
    if stackLst ==0:
        return "YES"
    else:
        return"NO"


vpsList = [input() for _ in range(n)]
for i in vpsList:
    print(isVps(i))


