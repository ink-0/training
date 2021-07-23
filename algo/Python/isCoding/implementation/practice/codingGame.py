def solution():
    n,m = map(int,input().split())
    x,y,v = map(int,input().split())
    #지나온 기록
    d = [[0]*m for _ in range(n)]
    direction = [[-1,0],[0,1],[1,0],[0,-1]]

    d[x][y]=1
    arr=[]
    #지도배열받기
    for i in range(n):
        temp = list(map(int,input().split()))
        arr.append(temp)
    cnt=0
    ans=1
    #왼쪽으로 도는 동작
    def turnLeft(v):
        v-=1
        if v == -1:
            v =3
        return v
    
    while True:
        v=turnLeft(v)
        addX,addY = direction[v]
        newX,newY = x+addX, y+addY

        if arr[newX][newY] ==0 and d[newX][newY]==0:
            d[newX][newY]=1
            x,y = newX,newY
            cnt=0
            ans+=1
            continue
        else:
            cnt+=1
        if cnt==4:
            backX,backY =direction[v]
            newX,newY = x-backX, y-backY 
            if arr[newX][newY] == 0:
                x,y = newX,newY
            else:
                break
            cnt=0
    print(ans)



# solution()
