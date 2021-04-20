import sys
input= sys.stdin.readline

n=int(input())

weight = list(int(input()) for _ in range(n))
weight.sort(reverse=True)
max_weight=0
for i in range(len(weight)):
    if max_weight<weight[i]*(i+1):
        max_weight=weight[i]*(i+1)
print(max_weight)

# weight.sort()
# weight_max=0
# for i in weight:
#     weight_max=max(i*n,weight_max)
#     n-=1
# print(weight_max)