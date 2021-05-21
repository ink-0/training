import sys
input = sys.stdin.readline
# n= int(input())
# end_time=0;
# cnt=0;

# Zoom = [list(map(int,input().split())) for i in range(n)]
# Zoom.sort(key=lambda x:(x[1],x[0]))


# for i in Zoom:
#     if(i[0]>=end_time):
#         cnt+=1
#         end_time=i[1]

# print(cnt)
#나중에 혼자 푸 것
all_time=[]
cnt=0
end_time=0
n=int(input())
for i in range(n):
    all_time.append(list(map(int,input().split())))

all_time.sort(key=lambda x: (x[1],x[0]))
for i in all_time:
    if(end_time<=i[0]):
        cnt+=1
        end_time=i[1]
print(cnt)
