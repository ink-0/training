def solution(a, b):
    answer=0
    for numA, numB in zip(a, b):
        print(numA, numB)
        answer+=numA*numB
    return answer

def solution2(a,b):
    return sum([x*y for x,y in zip(a,b)])