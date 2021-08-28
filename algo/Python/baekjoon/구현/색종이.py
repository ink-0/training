n = int(input())
paper = []

for i in range(n):
    paper.append(list(map(int,input().split())))


for i,p in enumerate(paper):
    cnt=0
    place = [[0]*1001 for _ in range(1001)]
    [row,col,area,height] = p
    for r in range(row,row+area):
        for c in range(col,col+height):
            place[r][c]=i+1

for i in range(n):
    cnt=0
    for p in place:
        cnt += p.count(i+1)
    print(cnt)



print('답',cnt)
    