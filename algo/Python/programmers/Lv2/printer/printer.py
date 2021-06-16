# def solution(priorities, location):
#     answer = 0

#     priIdx = [c for c in range(len(priorities))]  
#     priSort = sorted(priorities,reverse=True)
#     print(priSort)

#     i = 0
#     while True:
#         if priorities[i] < max(priorities[i+1:]):
#             priIdx.append(priIdx.pop(i))
#             priorities.append(priorities.pop(i))
#         else:
#             i += 1

#         if priorities == priSort:
#             break

#     return priIdx.index(location) + 1

def solution(priorities, location):
  answer = 0
  from collections import deque

  d = deque([(v,i) for i,v in enumerate(priorities)])

  while len(d):
      item = d.popleft()
      if d and max(d)[0] > item[0]:
          print("mas",max(d))
          d.append(item)
      else:
          answer += 1
          if item[1] == location:
              break
  return answer
print(solution([2,1,3,2],2))