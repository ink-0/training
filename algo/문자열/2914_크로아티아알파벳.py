import sys
input = sys.stdin.readline

# word = input().strip()

# cnt = len(word)

# for i in range(len(word)):
#     if i>0:
#         if word[i]=="-":
#             if word[i+1]=="c" or word[i-1]=="d":
#                 cnt-=1
#         elif word[i]=="j":
#             if word[i-1]=="l" or word[i-1]=="n":
#                 cnt-=1
#         elif word[i]=="=":
#             if word[i-1]=="c" or word[i-1]=="s":
#                 cnt-=1
#             elif word[i-1]=="z":
#                 cnt-=1
#                 if i>1:
#                     if word[i-2]=="d":
#                         cnt-=1
# print(cnt)

coratia=['c=','c-','dz=','d-','lj','nj','s=','z=']
word=input()

for i in coratia:
    word=word.replace(i,'?')
print(len(word))