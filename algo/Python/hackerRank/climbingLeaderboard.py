# 내 풀이 (이분탐색 직접)
def climbingLeaderboard(ranked, player):
    ans=[]
    ranked = sorted(list(set(ranked)))
    def bin_search(target,data):
        start = 0
        end = len(data)-1
        while start <= end:
            mid = (start+end)//2
            if data[mid] <= target:
                start=mid+1
            else:
                end=mid-1
        return start
    
    for i in player:
        ans.append(len(ranked)-bin_search(i,ranked)+1)
    
    return ans



# 다른풀이1 idx만 사용
# def climbingLeaderboard(ranked, player):
#     ranked = sorted(list(set(ranked)), reverse = True)
#     idx=len(ranked)
#     ans=[]
    
#     for i in player:
#         while idx>0 and ranked[idx-1]<=i:
#             idx-=1
#         if idx<0:
#             ans.append(1)
#             continue
#         ans.append(idx+1)
#     return ans

# 이분탐색 라이브러리 사용
# from bisect import bisect_right 

# def climbingLeaderboard(ranked,player):
#     ans=[]
#     ranked = sorted(set(ranked))
#     for p in player:
#         ans.append(len(ranked)-bisect_right(ranked,p)+1)     
#     return ans


ranked = [100,100,50,40,20,10]
player = [5,25,50,120]
print(climbingLeaderboard(ranked,player))