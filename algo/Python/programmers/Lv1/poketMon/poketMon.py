def solution(nums):

    setNums = list(set(nums))
    poketNum = int(len(nums)/2)

    if len(setNums)>= poketNum:
        return poketNum
    else:
        return len(setNums)


# def solution(nums):
#     return min(len(nums)/2, len(set(nums)))