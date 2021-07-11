import sys
input= sys.stdin.readline()

n = int(input())
nArr = sorted(list(map(int,input().split())))
m = int(input())
mArr=list(map(int,input().split()))


# def bin_search(target,data):
#         start = 0
#         end = len(data)-1
#         findSuc = 0
#         while start <= end:
#             mid = (start+end)//2
#             if data[mid] == target:
#                 findSuc = 1
#                 break

#             if data[mid] <= target:
#                 start=mid+1
#             else:
#                 end=mid-1
        
#         if findSuc:
#             return 1
#         else:
#             return 0
def bin_search(target,data):
    start = 0
    end = len(data)-1
    findSuc = 0
    while start <= end:
        mid = (start+end)//2
        if data[mid] == target:
            return 1
            break
        elif data[mid] <= target:
            start = mid +1
        else:
            end = mid-1
    return 0
for i in mArr:
    print(bin_search(i,nArr));

# from bisect  import bisect_left 


# for i in mArr:
#     nIdx=bisect_left (nArr,i)

#     if nIdx == len(nArr):
#         if i==nArr[-1]:
#             print(1)
#         else:
#             print(0)
#     # nIdx = bin_search(i,nArr)
#     else:
#         print(1)
