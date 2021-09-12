def solution(s):
    ans = len(s)

    for step in range(1,len(s)//2+1):
        compressed = ""
        prev = s[0:step]
        cnt=1

        for j in range(step, len(s) , step):
            if prev == s[j:j+step]:
                cnt+=1
            else:
                compressed += str(cnt) + prev if cnt>=2 else prev
                prev = s[j:j+step]
                cnt=1
        
        compressed += str(cnt) + prev if cnt >=2 else prev
        ans = min(ans, len(compressed))

    return ans
            
        

def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):

        cnt = 1
        ghStr = ''
        sliceArr = list(map(''.join, zip(*[iter(s)] * i)))
        prev = ''

        for word in sliceArr:
            if prev == word:
                cnt += 1
            else:
                if cnt == 1:
                    ghStr += prev
                else:
                    ghStr += str(cnt) + prev

                prev = word
                cnt = 1

        if cnt == 1:
            ghStr += prev
        else:
            ghStr += str(cnt) + prev

        temp = "".join(sliceArr)

        if len(s) != len(temp):
            ghStr += s[len(temp):]
        answer = min(len(ghStr), answer)

    return answer


# 0913 추가
import math
def solution(s):
    
    lenS = len(s)
    letterLen = []
    
    for i in range(1,math.ceil(lenS/2)+1):
        letter = ''
        cnt = 1
        
        for j in range(0,lenS-1,i):
            cur = s[j:j+i]
            nex = s[j+i:j+i+i]

            if cur == nex:
                cnt+=1
            elif cur != nex and cnt != 1:
                letter+=str(cnt)+cur
                cnt=1
            elif cur != nex and cnt == 1:
                letter +=cur
                
            if j==lenS-i-1:
                if cnt == 1:
                    letter+=nex 
                else:
                    letter+=str(cnt)+cur
                    
                    
        if letter == '':
            letterLen.append(len(s))
        else:
            letterLen.append(len(letter))

    return min(letterLen)