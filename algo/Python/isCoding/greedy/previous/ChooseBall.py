n,m = map(int,input().split())
ball = list(map(int,input().split()))
cnt=0
# for i in range(0,len(ball)-1):
#     for j in range(i+1,len(ball)):
#         if ball[i] != ball[j]:
#             cnt+=1
# print(cnt)
ans=0
array = [0] * 11
for i in ball:
    array[i]+=1

for i in range(1,m+1):
    n-=array[i] #총 개수 - i무게의 공 개수 제거
    ans += array[i]*n # i무게의 공개수 * i를제외한 공 총 개수
print(ans)