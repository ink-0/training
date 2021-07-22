def solution():
    n,k = map(int,input().split())
    cnt=0
    # while n!=1:
    #     if n%k ==0:
    #         n = n/k
    #         cnt+=1
    #     else:
    #         n-=1
    #         cnt+=1
    # print(cnt)

    while n >=k :
        while n%k!=0:
            n-=1
            cnt+=1
        n//=k
        cnt+=1
    while n>1:
        n-=1
        cnt+=1
    print(cnt)
solution()