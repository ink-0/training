def solution ():
    n,m = map(int,input().split())

    # for i in range(n):
    #     matrix.append(min(list(map(int, input().split()))))
    # print(max(matrix))
    result= 0
    for i in range(n):
        min_num = min(list(map(int,input().split())))
        
        result = max(result, min_num)
    print(result)


solution()
