def back (d,n,m):
    if d==m:
        print('********'
        ,*ans)
        return
    for i in range(n):
        if not visit[i]:
            visit[i]=True
            ans.append(i+1)

            back(d+1,n,m)

            ans.pop()
            visit[i]=False
        print('i',i,'ans',ans,'visit',visit)
            

n,m=map(int,input().split())
visit=[False]*n
ans=[]
back(0,n,m)