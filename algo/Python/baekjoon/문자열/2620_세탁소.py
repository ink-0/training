for _ in range(int(input())):
    C = int(input())
    d = [25, 10, 5, 1]
    li = []
    for n in d:
        li.append(C//n)
        C = C%n
    print(*li)