n = int(input())
paper = []

for i in range(n):
    paper.append(list(map(int,input().split())))


place = [[0]*10 for _ in range(10)]
for i,p in enumerate(paper):
    cnt=0
    [row,col,area,height] = p
    # for r in range(row,row+area):
    #     for c in range(col,col+height):
    #         place[r][c]=i+1

    for r in range(row,row+area):
        place[r][col:col+height] = [i+1]*height

for i in range(n):
    cnt=0
    for p in place:
        cnt += p.count(i+1)
    print(cnt)
