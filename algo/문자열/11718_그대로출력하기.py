import sys
input = sys.stdin.readline

while True:
    try:
        print(input())
    except EOFError:
        break

# for i in sys.stdin:
#     print(i)
# n=input()
# k=input()
# J=input()
# for i in n:
#     print(i)
# print(k+J)
