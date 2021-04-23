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
# for i in range(len(word)):
#     alphaDict[word[i]]=i
# alphaList = list(alphaDict.values())
# # for i in range(len(alphaList)):
# #     if(alphaList[i]==0):
# #         alphaList[i]=-1
# for i in range(len(alphaDict)):
#     print(alphaDict[i])


# print(*alphaList)



s=input()
ss=[]
for i in s:
    ss.append(ord(i))
   
c=set(ss)

ans=[]

for k in range(97,123):
    if k in c:
        print(ss.index(k),end=" ")
    else:
        print(-1,end=" ")