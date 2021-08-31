import re
s = input()

string = re.sub('\d','',s)
number = re.sub('\D','',s)

sum_num = sum(list(map(int,list(number))))
print(''.join(sorted(string))+str(sum_num))


ans=''
val=0
for i in s:
    if s.isalpha():
        ans.append(i)
    else:
        val+=int(i)
ans.sort()

if val !=0:
    ans.append(str(val))

print(''.join(ans))