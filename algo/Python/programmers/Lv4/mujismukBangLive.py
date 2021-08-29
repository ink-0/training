# def solution(food_times, k):
#     answer = 0
#     cur_food=0
#     cur_time=0
    
#     def isNotNetworkError(ct):
#         if ct<= k:
#             return True
#         else:
#             return False
    
#     while isNotNetworkError(cur_time):
#         for idx,f in enumerate(food_times):
#             if f!=0:
#                 cur_time+=1
#                 food_times[idx]-=1
#                 cur_food=idx+1
#                 # print('1번째',food_times,'idx',idx,'cur_time',cur_time)
#             else:
#                 # print('2번째',food_times,'idx',idx,'cur_time',cur_time)
#                 continue
#             if isNotNetworkError(cur_time)==False:
#                 # print('---------넘은경우',food_times,'idx',idx,'cur_time',cur_time)
#                 break
                

#     if cur_time == k+1:
#         return(cur_food)
#     else:
#         return(-1)
    

def solution(food_times, k):
    
    start,end = 0,100000000
    food_len, cutting, idx= len(food_times),0,0
    
    while start <= end:
        mid = (start+end)//2
        last_second = food_len * mid
        
        for f in food_times:
            temp = f-mid
            if temp <0 :
                last_second += temp
        if last_second <= k:
            cutting, idx= mid, last_second
            start = mid+1
        else:
            end = mid-1
    food_times = [f-cutting for f in food_times]
    
    for i in range(food_len):
        if food_times[i] > 0 and idx==k:
            return i+1
        else:
            if food_times[i]>0:
                idx+=1
    return -1