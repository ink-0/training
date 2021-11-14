testCase = int(input())

for tc in range (1,testCase+1):
    n = int(input())
    str = input()
    wordList = set()

    for i in range (len(str)):
        for j in range (i+1,len(str)+1):
            temp = str[i:j]
            wordList.add(temp)

    wordList = sorted(wordList)
    if n > len(wordList):
        n = n%len(wordList)
    print(f'#{tc} {"".join(wordList[n-1])}')