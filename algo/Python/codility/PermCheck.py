def solution(A):
    A.sort()
    if A[0]==1:
        if len(A)<2:
            return 1
        else:
            for i in range(len(A)-1):
                if A[i]+1==A[i+1]:
                    ans=1
                else:
                    ans=0
                    break
            return ans
    else:
        return 0

def solution(A):
    if max(A)!=len(A) or len(A)!=len(set(A)):
        return 0
    return 1

print(solution([2,3,4,5]))