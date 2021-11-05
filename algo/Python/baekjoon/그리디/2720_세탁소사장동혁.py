import sys

input = sys.stdin.readline
T = int(input())

for i in range(T):
    C = int(input())
    ans = [0, 0, 0, 0]
    changes = [25, 10, 5, 1]
    for c in range(len(changes)):
        ans[c] += C // changes[c]
        C %= changes[c]

    print(*ans)