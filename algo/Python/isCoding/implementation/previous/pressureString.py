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
        