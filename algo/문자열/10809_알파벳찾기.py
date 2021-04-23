import sys
import string

# alphaDict={}
# input = sys.stdin.readline
# alpha = list(string.ascii_lowercase)
# word = input().strip()
# ans=[]
# for i in alpha:
#     if(i in word):
#         ans.append(word.index(i))
#     else:
#         ans.append(-1)

# print(*ans)


# asciiList=[]
# for i in word:
#     asciiList.append(ord(i))

# asciiSet = set(asciiList)
# for j in range(97,123):
#     if j in asciiSet:
#         print(asciiList.index(j),end=" ")
#     else:
#         print(-1,end=" ")

list = [-1]*26
word = [ord(i)-ord('a') for i in input()]

for i,v in enumerate(word):
    if(list[v]==-1):
        list[v]=i

print(*list)