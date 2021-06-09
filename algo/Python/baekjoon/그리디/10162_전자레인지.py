import sys
input= sys.stdin.readline

time=int(input())
bag=0
rangeLst = [300,60,10]
ansLst=[0,0,0]

while time>=0:
    if time>=rangeLst[0]:
        ansLst[0]=(time//rangeLst[0])
        time = time%rangeLst[0]
    elif time >= rangeLst[1] and time < rangeLst[0]:
        ansLst[1]=(time//rangeLst[1])
        time = time%rangeLst[1]
    elif time >= rangeLst[2] and time < rangeLst[1]:
         ansLst[2]=(time//rangeLst[2])
         time = time%rangeLst[2]
    elif time < rangeLst[2] and time!=0:
        print('-1')
        break
    else :
        print(*ansLst)
        break


    
# T = int(input())

# if T % 10 != 0:
#     print(-1)
# else:
#     A = B = C = 0
#     A = T // 300
#     B = (T % 300) // 60
#     C = (T % 300) % 60 // 10
#     print(A, B, C)