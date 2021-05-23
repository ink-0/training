def getKey(num):
        keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
        for idx,lst in enumerate(keypad):
            if num in lst:
                print(idx,lst.index(num))
                return [idx,lst.index(num)]

def getLenKey(key1,key2):
    xLen = abs(key1[0]-key2[0])
    yLen = abs(key1[1]-key2[1])
    return xLen+yLen
    

def solution(numbers, hand):
    answer = ''
    cur_left= '*'
    cur_right='#'
    
    print(getKey(6))
    
    for num in numbers:
        boundary=num%3
        if boundary == 1 :
            answer+='L'
            cur_left = num
        elif boundary == 0 and num!= 0:
            answer+='R'
            cur_right = num
        else:
            key_right = getKey(cur_right)
            key_left = getKey(cur_left)
            key_num = getKey(num)
            len_right = getLenKey(key_right,key_num)
            len_left = getLenKey(key_left,key_num)
            
            if len_right < len_left :
                answer+='R'
                cur_right = num
            elif len_right > len_left:
                answer += 'L'
                cur_left = num
            else:
                if hand == 'right':
                    answer+='R'
                    cur_right = num
                else:
                    answer += 'L'
                    cur_left = num
    return answer
                    
            

            
