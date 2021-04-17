import sys
input = sys.stdin.readline

n=int(input())
word_arr= [input().strip() for i in range(n)]
word_arr=set(word_arr)
word_arr=list(word_arr)
word_arr.sort(key=lambda x:(len(x),x))


for i in word_arr:
    print(i)