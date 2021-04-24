n= int(input())


def isVps(word):
    psL="("
    psR=")"
    cnt=0;
    if(word.count(psL)!=word.count(psR)):
        return "No"
    elif word[-1]==psL:
        return "No"
    else:
        return"YES"




vpsList = [input() for _ in range(n)]
for i in vpsList:
    print(isVps(i))