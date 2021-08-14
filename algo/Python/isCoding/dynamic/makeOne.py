# def solution(num):
#     cnt=0
#     def calculate(x):
#         if x%5==0:
#             print('1')
#             return x//5
#         elif x%3==0:
#             print('2')
#             return x//3
#         elif x%2==0:
#             print('3')
#             return x//2
#         elif x>1:
#             return x-1
#     while num!=1:
#         num = calculate(num)
#         print('num----',num)
#         cnt+=1
#     print(cnt)

def solution():
    x=  int(input())
    d = [0]*30001

    for i in range(2,x+1):
        d[i] = d[i-1]+1
        if i%2 == 0:
            d[i]= min(d[i],d[i//2]+1)
        if i%3 ==0:
            d[i] = min(d[i],d[i//3]+1)
        if i%5 ==0 :
            d[i] = min(d[i],d[i//5]+1)
    print(d[x],i)

solution()
    