def solution(arr1, arr2):
    answer = []
    lenArrOne = len(arr1)
    lenArrTwoIn = len(arr2[0])
    lenArrTwo=len(arr2)
    

    for i in range(lenArrOne):
        tempLst = []
        for j in range(lenArrTwoIn):
            cnt=0
            for k in range(lenArrTwo):
                cnt+=arr1[i][k]*arr2[k][j]
            tempLst.append(cnt)
        answer.append(tempLst)
            
        
        
    return answer
