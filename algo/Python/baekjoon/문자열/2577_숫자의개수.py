import sys
input  = sys.stdin.readline
 
# num = [int(input()) for _ in range(3)]
# ans=num[0]*num[1]*num[2]


# cntArr = [0]*10

# for i in str(ans):
#     cntArr[int(i)]+=1

# for i in cntArr:
#     print(i)
a=int(input())
b=int(input())
c=int(input())

mul=str(a*b*c)

for i in range(10):
    print(mul.count(str(i)))
