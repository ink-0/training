

data = list(map(int,list(input())))
ans=0
for i in data:
    if i <=1 or ans <=1:
        ans+=i
    else:
        ans*=i
print(ans)



