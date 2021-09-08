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

def solution(s):
    result=[] 
    if len(s)==1: 
        return 1 
    for i in range(1, (len(s)//2)+1): 
        b = '' 
        cnt = 1 
        tmp=s[:i] 
        
        for j in range(i, len(s), i): 
            if tmp==s[j:i+j]: 
                cnt+=1 
            else: 
                if cnt!=1: 
                    b = b + str(cnt)+tmp 
                else: 
                    b = b + tmp 
                    tmp=s[j:j+i] 
                    cnt = 1 
        if cnt!=1: 
            b = b + str(cnt) + tmp 
        else: 
            b = b + tmp 
            result.append(len(b)) 
        return min(result)

