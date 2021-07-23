def solution ():
    n = int(input())
    go = input().split()
    loc = [1,1]

    for i in go:
        if i == 'R':
            if loc[1]+1<=n:
                loc[1]+=1
        elif i == 'L':
            if loc[1]-1>1:
                loc[1]-=1
        elif i == 'U':
            if loc[0]-1>1:
                loc[0]-=1
        else:
            if loc[0]+1<n:
                loc[0]+=1
    print(" ".join(map(str,loc)))

        
solution()
