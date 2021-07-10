# 내풀이 퀵정렬, 이분탐색 사용해봄 시간초과
# def climbingLeaderboard(ranked, player):
    
#     # def quick_sort(array):
#     #     if len(array) <= 1:
#     #         return array

#     #     pivot = array[0]
#     #     tail = array[1:]

#     #     left_side = [x for x in tail if x <= pivot]
#     #     right_side = [x for x in tail if x > pivot]

#     #     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#     def bin_search (target,data):
#         data.sort(reverse=True)
#         start=0
#         end=len(data)-1
#         while start<=end:
#             mid = (start+end) // 2
#             if data[mid] == target:
#                 return mid
#             elif data[mid]>target:
#                 start=mid+1
#             else:
#                 end=mid-1
        
#     ans=[]
#     for i in player:
#         ranked.append(i)
#         ranked =list(set(ranked))
#         # ranked=quick_sort(ranked)
#         # ranked.sort(reverse=True)
       
#         ans.append(bin_search(i,ranked)+1)
#     return ans



#다른풀이
def climbingLeaderboard(ranked, player):
    ranked = sorted(list(set(ranked)), reverse = True)
    idx=len(ranked)
    ans=[]
    
    for i in player:
        while idx>0 and ranked[idx-1]<=i:
            idx-=1
        if idx<0:
            ans.append(1)
            continue
        ans.append(idx+1)
    return ans


ranked = [100,100,50,40,20,10]
player = [5,25,50,120]
print(climbingLeaderboard(ranked,player))