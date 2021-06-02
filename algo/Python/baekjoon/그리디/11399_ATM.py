import sys
input= sys.stdin.readline

#오름차순으로 변경
# 누적값 전부 더학
cnt=0
sumArr=[]
n=int(input())
man=input()
# manLst = man.strip().split(' ')
# manLst = list(map(int,manLst))
# manLst.sort()

manLst = sorted(list(map(int,input().split())))


for man in manLst:
    sumArr.append(man)
    cnt+=sum(sumArr)
    # print(sum([p*(N-i) for i, p in enumerate(P)]))
print(cnt)

# 1차시도) sumArr에 인수 하나씩 더해서 sum을 해준다 
# 2차 시도) ans 과 sumans 변수 2개를 만들어 각자 더해줌

