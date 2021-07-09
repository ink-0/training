def solution(A):
    A=list(set(A))
    A.sort()
    smallNum=1
    for i in A:

        if smallNum ==i:
            smallNum+=1

    return smallNum