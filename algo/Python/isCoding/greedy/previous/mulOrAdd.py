
data = list(input())
ans=0
for i in range(1,len(data)):
    num = int(data[i])
    if num <=1 or ans <=1:
        ans+=num
    else:
        ans*=num
print(ans)

