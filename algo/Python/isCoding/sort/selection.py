array = [3,4,2,6]

# for i in range(len(array)):
#     min_idx=i
#     for j in range(i+1,len(array)):
#         if array[j]<array[min_idx]:
#             min_idx = j
#     array[i],array[min_idx] = array[min_idx],array[i]


# for i in range(len(array)):
#     for j in range(i,0,-1):
#         if array[j]<array[j-1]:
#             array[j],array[j-1] = array[j-1],array[j]

# def quick(array):
#     if len(array)<=1:
#         return array

#     pivot = array[0]
#     tail = array[1:]

#     leftArr =  [ t for t in tail if t<= pivot]
#     rightArr =  [ t for t in tail if t>pivot]

#     return quick(leftArr)+ [pivot]+quick(rightArr)
# print(quick(array))

def idxSort(array):
    cnt = [0]* (max(array)+1)
    for i in range(len(array)):
        cnt[array[i]]+=1
    
    for i in range(len(cnt)):
        for j in range(cnt[i]):
            print(i, end=' ')

print(idxSort(array))