# 문자열 압축

[링크](https://programmers.co.kr/learn/courses/30/lessons/60057)

### 📌 내 풀이 (오답) 첫번째

```py
def solution(s):
    answer = 0
    summaryLst=[]
    for i in range(1, len(s)//2+1):
        if i ==1:
            length=i
            compareZone=['']
            sliceArr=list(map(''.join, zip(*[iter(s)]*length)))
            cnt=0
            for word in sliceArr:
                if compareZone[0]==word:
                    cnt+=1
                else:
                    compareZone[0]=word
            if cnt!=0:
                summaryLst.append(len(s)-i*cnt+cnt-1)
            else:
                summaryLst.append(len(s))
        else:
            length=i
            compareZone=['']
            sliceArr=list(map(''.join, zip(*[iter(s)]*length)))
            cnt=0
            for word in sliceArr:
                if compareZone[0]==word:
                    cnt+=1
                else:
                    compareZone[0]=word
            if cnt!=0:
                summaryLst.append(len(s)-i*cnt+cnt)
            else:
                summaryLst.append(len(s))

    return min(summaryLst)


```

#### 처음 생각한 로직

1. 1부터 길이의 반개까지
2. return 값 총길이 - 단위 \* (단위가 나온 개수) +단위가 나온 개수
   - 16 8개 16-8\*1+1
   - 10 2개 8 10-3\*(2)+1
3. 모든 경우의 수를 return에 넣어서 제일 작은 수 빼기
   코드 실행했더니 실패  
   간과한 부분은 **cnt를0부터센것** , **공식을만들려한것**

### 📌 내 풀이 두번째

```py
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
```

<br>

### 📌 다른 풀이

```py
def solution(s):
    wordLenArr=[]
    result=''

    if len(s)==1:
        return 1;
    for cut in range(1, len(s)//2+1):
        cnt=1
        tempStr = s[:cut]
        for i in range(cut,len(s),cut):
            if tempStr == s[i:i+cut]:
                cnt+=1
            else:
                if cnt==1:
                    cnt=''
                result+=str(cnt)+tempStr
                tempStr = s[i:i+cut]
                cnt=1

        if cnt ==1 :
            cnt=''
        result += str(cnt)+tempStr
        wordLenArr.append(len(result))
        result=''
    return min(wordLenArr)

```
