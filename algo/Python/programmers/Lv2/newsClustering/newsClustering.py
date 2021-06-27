
# import re

# def solution(str1, str2):
#     str1Arr=[]
#     str2Arr=[]
    
#     for i in range(len(str1)-1):
#         alpha = re.sub('[^a-zA-z]|\^','',str1[i:i+2])
#         if len(alpha)>=2:
#             str1Arr.append(alpha.upper())

#     for j in range(len(str2)-1):
#         alpha = re.sub('[^a-zA-z]|\^','',str2[j:j+2])

#         if len(alpha)>=2:
#             str2Arr.append(alpha.upper())
            
#     if len(str1Arr)==0 and len(str1Arr)==0:
#         return 65536
#     common = []
#     cstr1Arr = str1Arr.copy()
#     union= str1Arr.copy()
#     #합집합 
#     for i in str2Arr:
#         if i not in cstr1Arr:
#             union.append(i)
#         else:
#             cstr1Arr.remove(i)
    
#     #교집합
#     for i in str2Arr:
#         if i in str1Arr:
#             str1Arr.remove(i)
#             common.append(i)
#     return int(len(common)/len(union)*65536)
import re
def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if not re.findall('[^a-zA-Z]',str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if not re.findall('[^a-zA-Z]',str2[i:i+2])]

    
    intersection = list(set(str1) & set(str2))
    union = list(set(str1) | set(str2))
    
    
    lenInter = sum([min(str1.count(i), str2.count(i)) for i in intersection ])
    lenUnion = sum([max(str1.count(i), str2.count(i)) for i in union ])
    if lenUnion==0:
        return 65536
    
    return int(lenInter/lenUnion*65536)