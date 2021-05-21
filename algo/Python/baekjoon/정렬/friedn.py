#idx>=그 값의 수
#각 숫자가 처음 나왓을때 건ㄴ너건너 있는지 확인

n=int(input())
a=[1,3,2,2,1]
count=0
for i in range(len(a)):
    if(i<=len(a)):
        if(i+1>=a[i]):
            print("😎",i,"번째",a[i])
            count+=2
        else:
            count+=1
    else:
        if(len(a)-i+1>=a[i]):
            print("🔥",i,"번째",a[i])
            count+=2
        else:
            count+=1
print(count)

