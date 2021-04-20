import sys
input = sys.stdin.readline

# def binarySearch(list,ele,start,end):
#     while start<=end:
#         mid = (start+end)//2
#     if ele == list[mid]:
#         return True
#     if ele > list[mid]:
#         start+=1
#     else:
#         end-=1

#     return False
def binarySearch(list,target,low,high):
    while low<=high:
        mid = (low+high)//2
        if list[mid] == target:
            return True
        if target > list[mid]:
            low = mid+1
        else:
            high = mid-1

    return False



h,s = map(int,input().split())

hList = [input().strip() for _ in range(h)]
sList = [input().strip() for _ in range(s)]
hList.sort()

ans=[]
for i in sList:
    if binarySearch(hList, i, 0,h-1):
        ans.append(i)
print(len(ans))
for i in sorted(ans):
    print(i)


# hSet=set(hList)
# sSet=set(sList)

# ans=[]
# ans = sorted(list(hSet & sSet))
# print(len(ans))
# for i in ans:
#     print(i.strip())
