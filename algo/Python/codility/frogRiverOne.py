def solution(X, A):
    idArr = [0]*X
    idSum=0

    for i in range(len(A)):
        if idArr[A[i]-1]==0:
            idArr[A[i]-1]=1
            idSum+=1

        if idSum==X:
            return i
    return -1
