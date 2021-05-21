
import sys
input = sys.stdin.readline
n  = int(input())
num_arr = [int(input()) for i in range (n)]
num_arr.sort()
for i in num_arr:
    print(i)