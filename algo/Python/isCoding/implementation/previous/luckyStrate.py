n = input()
half = len(n)//2

# first = n[:half]
# last = n[half:]

# first_sum = sum(list(map(int,list(first))))
# last_sum = sum(list(map(int,list(last))))

# if first_sum == last_sum:
#     print('LUCKY')
# else:
#     print('READY')
summary = 0
for i in range(half):
    summary += int(n[i])

for i in range(half, len(n)):
    summary -= int(n[i])

if summary == 0:
    print('LUCKY')
else:
    print('READY')


