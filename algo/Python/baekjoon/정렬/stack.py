n=int(input())
count=0
a=[27,46,47,10,17,35,10,32,46,23,36,17,44,36,15,42]
# a=[4,2,5,3,1]

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if(a[i]<a[j] and a[i]>a[k]):
                print(a[i],a[j],a[k])
                count+=1
                
print(count)

