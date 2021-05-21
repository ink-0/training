import sys
input = sys.stdin.readline

# n= int(input())
# cnt=0
# def isGroup(word):
#     checkList=[]
#     for j in word:
#         if j in checkList and j!=checkList[-1]:
#             return False
#         else:
#             checkList.append(j)
#             continue
#     return 1

# for i in range(n):
#     word=input().strip()
#     if isGroup(word):
#         cnt+=1
# print(cnt)

# cnt=0
# n=int(input())

# for i in range(n):
#     wCheck=0
#     word=input().strip()
#     sWord = word

#     for j in sWord:
#         if j in word:
#             g1=word.count("*")
#             word=word.replace(j,"*")
#             g2=word.count("*")
#             diff = g2-g1

#             if diff>1:
#                 if "*" not in word[g1+diff:]:
#                     wCheck+=diff
#             else:
#                 wCheck+=1
    
#     if wCheck == len(word):
#         cnt+=1
# print(cnt)


n=int(input())
wordLst=[]
for _ in range(n):
    wordLst.append(input().strip())

cnt=0
for word in wordLst:
    ans=[]
    cnt+=1
    cur=word[0]
    for i in word:
        if cur==i:
            continue
        elif i in ans:
            cnt-=1
            break
        else:
            ans.append(cur)
            cur=i
print(cnt)