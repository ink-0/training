import sys
input = sys.stdin.readline
n= int(input())
end_time=0;
cnt=0;

Zoom = [list(map(int,input().split())) for i in range(n)]
Zoom.sort(key=lambda x:(x[1],x[0]))


for i in Zoom:
    if(i[0]>=end_time):
        cnt+=1
        end_time=i[1]

print(cnt)


