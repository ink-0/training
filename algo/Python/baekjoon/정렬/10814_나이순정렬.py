import sys
input = sys.stdin.readline

n  = int(input())
members = [list(input().split()) for _ in range(n)]
members.sort(key=lambda x: (int(x[0])))
for i in members:
    print(*i)

# for i in range(n):
#     a,b=input().split()
#     members.append([int(a),b])