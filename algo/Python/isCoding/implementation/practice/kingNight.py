def solution():
    inp = input()
    colArr= ['a','b','c','d','e','f','g','h']
    col,row = inp[0],int(inp[1])
    # col = colArr.index(col)+1
    col = ord(col)-ord(colArr[0])+1
    move = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
    cnt=0

    for m in move:
        tCol = col+m[0] 
        tRow = row+m[1]
        if tCol>0 and tRow>0 and tCol<9 and tRow<9:
            cnt+=1
    print(cnt)
solution()