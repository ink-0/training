import sys
input = sys.stdin.readline

num=int(input())
newNum=num
# fn=num//10 
# sn=num%10
# add=fn+sn
# newNum = sn*10+add%10

count=1


# while num!=newNum:
#     fn=newNum//10 
#     sn=newNum%10
#     add=fn+sn
#     newNum = sn*10+add%10
#     count+=1
# print(count)

while (True):
    fn=newNum//10 
    sn=newNum%10
    add=fn+sn
    newNum = sn*10+add%10
    if newNum==num:
        break
    count+=1
print(count)
