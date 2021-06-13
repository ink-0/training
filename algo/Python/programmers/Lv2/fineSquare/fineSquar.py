from math import gcd
def solution(w,h):
    delSquerCnt = w+h-gcd(w,h)
    return w*h-delSquerCnt