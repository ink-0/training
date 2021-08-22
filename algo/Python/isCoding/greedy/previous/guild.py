n = int(input())
guild = list(map(int,input().split()))

guild.sort()

cnt=0
ans=0
for i in guild:
    cnt+=1
    if cnt >= i:
        ans+=1
        cnt=0
print(ans)

