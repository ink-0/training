# 모든 두가지 수를 더한 값을 구함
# k로 나눠지는지 확인
# 나눠지는 애들이 포함된 구성요소들 제거
from itertools import combinations

# def nonDivisibleSubset(k, s):
#     ans=[]
#     nonMul = []
#     twoSet = list(combinations(s,2))
#     for i,j in twoSet:
#         print(i,j,'=',i+j,'나누기',(i+j)%k)
#         if (i+j)%k !=0:
#             nonMul.append([i,j])

#     return nonMul

def nonDivisibleSubset(k, s):
    remainder_cnt = {}
    answer = 0

    # k로 나눈 나머지를 dictionary에 저장
    for num in s:
        remainder = num % k
        if remainder in remainder_cnt:
            remainder_cnt[remainder] = remainder_cnt[remainder] + 1
        else:
            remainder_cnt[remainder] = 1
    print('리마인더',remainder)
    for remainder in range((k+1)//2, k):
        opposite_remainder = k - remainder
        if remainder == opposite_remainder and remainder in remainder_cnt:
            answer += 1
            continue


        if remainder in remainder_cnt and opposite_remainder in remainder_cnt:
            answer += max(remainder_cnt[remainder], remainder_cnt[opposite_remainder])
        elif remainder in remainder_cnt:
            answer += remainder_cnt[remainder]
        elif opposite_remainder in remainder_cnt:
            answer += remainder_cnt[opposite_remainder]

    if 0 in remainder_cnt:
        answer += 1

    return answer


# k=7
# s=[278, 576, 496, 727, 410 ,124 ,338 ,149, 209 ,702 ,282 ,718 ,771, 575, 436]
k=3
s=[1, 7, 2, 4]
print(nonDivisibleSubset(k,s))