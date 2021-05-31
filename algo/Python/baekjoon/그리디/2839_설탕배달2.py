import sys
input= sys.stdin.readline

# 3가지로 나누기
# 3,5 
# 3
#5
sugar=int(input())
bag=0

while sugar>=0:
    if sugar%5==0:
        bag+=(sugar//5)
        print(bag)
        break
    sugar-=3
    bag+=1
else:
    print(-1)

    
