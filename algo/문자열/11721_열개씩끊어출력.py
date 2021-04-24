import sys
import math
input = sys.stdin.readline
word = input().strip()

for i in range(math.ceil(len(word)/10)):
    print(word[10*i:10*(i+1)])