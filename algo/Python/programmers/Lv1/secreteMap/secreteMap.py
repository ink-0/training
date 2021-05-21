
def checkbinLen (binNum,n):
    while len(binNum)<n:
            binNum='0'+binNum
    return binNum

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        arr1binNum = format(arr1[i],'b')
        arr2binNum = format(arr2[i],'b')
        arr1binNum = checkbinLen(arr1binNum,n)
        arr2binNum = checkbinLen(arr2binNum,n)
        
        bin2wall=''
        for j in range(n):
            if (int(arr1binNum[j])+int(arr2binNum[j]))>0 :
                bin2wall+='#'
            else:
                bin2wall+=' '
        answer.append(bin2wall)
        
    return answer
    # return answer
   # 각 숫자 이진수로 변경
    # 각 자릿수 or 로 해줌
    # 1 -> "#", 0 => " "변경
    