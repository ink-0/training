# print("this is a debug message")
# p,q를동시에 돌면서 두가지값을 빼서
# S 에서슬라이싱을한다.
# 그 값들의 발류를찾는다
# 거기서 최소값을 ansdps jgsmsek

# def solution(S, P, Q):
#     dObj = {'A':1,'C':2,'G':3,'T':4}
#     ansArr =[]

#     for i,j in zip(P,Q):
#         if i==j:
#             ansArr.append(dObj[S[i]])
#         else:
#             tempArr=[]
#             for k in S[i:j]:
#                 tempArr.append(dObj[k])
#             ansArr.append(min(tempArr))
#     return(ansArr)

def solution(S, P, Q):
    dObj = {'A':1,'C':2,'G':3,'T':4}
    ans =[]

    for i,j in zip(P,Q):
        minNum=5
        if i==j:
            ans.append(dObj[S[i]])
        else:
            if 'A' in S[i:j+1]:
                num = 1
            elif 'C' in S[i:j+1]:
                num = 2
            elif 'G' in S[i:j+1]:
                num = 3
            elif 'T' in S[i:j+1]:
                num = 4
            
            if minNum > num:
                minNum = num
            ans.append(minNum)

    return(ans)