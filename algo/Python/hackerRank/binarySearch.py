# bisect_right : start
# bisect_left : end
# 존재하는 값만 찾을 때 : end 
arr = [1,2,4,5,7]
def bin_search(target,data) :
    start=0
    end=len(data)-1

    while(start<=end):
        mid=(start+end)//2

        if data[mid] <=target:
            start=mid+1
        else:
            end=mid-1
        
    print(start, end, mid)
    return end


# data=[1,3,5,9]
# target1=1
# target2=2
# target3=3
# target4=4


# print('같은거: 1-----',bin_search(target1,data))
# print('다른거: 2-----',bin_search(target2,data))
# print('같은거: 3-----',bin_search(target3,data))
# print('다른거: 4-----',bin_search(target4,data))

# arr = [1,2,4,5,7] 

from bisect  import bisect_right 
print('라이브러리',bisect_right(arr,4))
print('라이브러리',bisect_right(arr,3))


print(bin_search(4,arr));
print(bin_search(3,arr));