def solution(N):

    binArr = [b for b in bin(N)[2:]]
    binCnt= binArr.count('1')

    if binCnt==0 or binCnt==len(binArr) or binCnt==1:
        return 0

    else:
        oneArr=[]
        gapArr=[]
        for i in range(len(binArr)):
            if binArr[i]=='1':
                oneArr.append(i)

        for j in range(len(oneArr)-1,0,-1):
            gapArr.append(oneArr[j]-oneArr[j-1]-1)
        return max(gapArr)
