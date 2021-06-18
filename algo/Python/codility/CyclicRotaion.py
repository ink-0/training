
def solution(A, K):
    if len(A)==0: # 빈 배열이 나왓을 때
        return []
    else:
        for i in range(K):
            A.insert(0,A.pop(-1))
        return A
