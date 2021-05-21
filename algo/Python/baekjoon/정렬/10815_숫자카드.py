import sys
input = sys.stdin.readline

# def bin_search (ele,sort_list,start=0,end=None):
#     if end == None:
#         end = len(sort_list) - 1
#     if start > end:
#         return 0
#     mid=(start+end)//2

#     if ele == sort_list[mid]:
#         return 1
#     elif ele < sort_list[mid]:
#         end=mid-1
#     elif ele > sort_list[mid]:
#         start = mid+1
#     return bin_search(ele,sort_list,start,end)

n=int(input())
card_list = list(map(int,input().split()))
m=int(input())
check_list = list(map(int,input().split()))

# card_list.sort()
# ans=[]
# for i in check_list:
#     ans.append(bin_search(i, card_list))

# print(" ".join(map(str,ans)))

check_dict = { i:0 for i in check_list}

for i in card_list:
    if(i in check_dict.keys()):
        check_dict[i]=1

print(" ".join(list(map(str,check_dict.values()))))