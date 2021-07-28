# 그냥 이중 for문으로 하면 O(n^2)
# def solution():
#     n = int(input())
#     store_part =list(map(int,input().split()))
#     m = int(input())
#     find_part =list(map(int,input().split()))

#     def bin_search(target,data,start,end):
#         while start <= end:
#             mid = (start+end)//2

#             if data[mid]== target:
#                 return mid
#             elif data[mid]<target:
#                 start = mid+1
#             elif data[mid]>target:
#                 end = mid-1
#         return None
    
#     for i in range(m):
#         result = bin_search(find_part[i],store_part,0,n-1)
#         if result != None:
#             print('yes',end= ' ')
#         else:
#             print('no',end= ' ')

def solution():
    n = int(input())
    # store_part =list(map(int,input().split()))

    arr = [0]*1000000
    for i in input().split():
        arr[int(i)] = 1

    m = int(input())
    find_part =list(map(int,input().split()))

    for f in find_part:
        if arr[f] ==1:
            print('yes',end= ' ')
        else:
            print('no',end= ' ')



    

solution()