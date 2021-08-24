st = list(map(int,list(input())))
# cnt=0
# for i in range(0,len(st)-1):
#     if st[i]!= st[i+1]:
#         cnt+=1
# print(cnt-1)    
cnt0 = cnt1 = 0

if st[0] == 1:
    cnt0+=1
else:
    cnt1+=1

for i in range(0, len(st)-1):
    if st[i] != st[i+1]:
        if st[i+1] == 1:
            cnt0+=1
        else:
            cnt1+=1

print(min(cnt0,cnt1))