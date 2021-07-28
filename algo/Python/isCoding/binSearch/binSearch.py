def bin_search(target,data,start,end):
    while start <= end:
        mid = (start+end)//2

        if data[mid]== target:
            return mid
        elif data[mid]<target:
            start = mid+1
        elif data[mid]>target:
            end = mid-1
    return None
result = bin_search(3,[2,3,4,5,6],0,4)
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result+1)
from bisect import bisect_left

arr=[ 2,3,4,5,6]
print(bisect_left(arr,4))
