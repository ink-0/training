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
        #마지막 글자의 개수까지 더해줌
        if cnt == 1:
            ghStr += prev
        else:
            ghStr += str(cnt) + prev

        temp = "".join(sliceArr)
        # sliceArr 에서 잘린 부분이 있어서 해당 부분 추가
        if len(s) != len(temp):
            ghStr += s[len(temp):]
        answer = min(len(ghStr), answer)

    return answer