import sys
input= sys.stdin.readline


def divFive(num):
    return int(num%5)
def divThree(num):
    return int(num%3)

n = int(input())
cnt=0
m=n
while m>=3:
    while m>=5:
        cnt+=1
        m-=5
    cnt+=1
    m-=3
if(m!=0):
    cnt=0
    while n>=3:
        cnt+=1
        n-=3
    if(n!=0):
        print(-1)
    else:
        print(cnt)
else:
    print(cnt)
    
    

