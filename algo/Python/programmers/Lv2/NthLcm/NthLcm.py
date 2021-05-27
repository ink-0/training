from math import gcd
def solution(arr):
    def lcm(x,y):
        return x*y//gcd(x,y)
    
    while len(arr) >1:
        arr.append(lcm(arr.pop(),arr.pop()))
        
    return arr[0]
# from fractions import gcd


# def nlcm(num):      
#     answer = num[0]
#     for n in num:
#         answer = n * answer / gcd(n, answer)

#     return answer