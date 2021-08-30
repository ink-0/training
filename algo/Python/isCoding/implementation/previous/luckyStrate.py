n = input()
half = len(n)//2

first = n[:half]
last = n[half:]
print(last)

first_sum = sum(list(map(int,list(first))))
last_sum = sum(list(map(int,list(last))))

print(first_sum,last_sum)
if first_sum == last_sum:
    print('LUCKY')
else:
    print('READY')



