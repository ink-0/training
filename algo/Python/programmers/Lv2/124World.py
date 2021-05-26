def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        print('n',n,'글자','124'[n%3])
        answer = '124'[n%3] + answer
        print("answer",answer)
        n //= 3
        print("2n",n)
    return answer

# def solution(n):
#     answer = ''
#     strN = str(n)
#     otfArr = ['0','1','2','4','11','12','14','21','22','24','41']
    
#     for i in range(len(strN)):
#         # print(strN[i])
#         # if strN[i]=='1' and strN[i+1]=='0':
#         #     answer+=otfArr[10]
#         #     del strN[i+1]
#         # else:
#         answer+=otfArr[int(strN[i])]

#     return str(answer)