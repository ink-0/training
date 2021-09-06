def solution(s):
    ans = len(s)

    for step in range(1,len(s)//2+1):
        compressed = ""
        prev = s[0:step]
        prev = s[0:step]
        cnt=1

        for j in range(step, len(s) , step):
            if prev == s[j:j+step]:
                cnt+1
        

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