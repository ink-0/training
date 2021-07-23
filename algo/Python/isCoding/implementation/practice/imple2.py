# ##5시 59분 59초
# # 3 13 23 33 43 53 31 32 34 35 36 37 38 39 
# # 24 * 60 * 60 
# 3 13 23 33 43 53 30 31 32 34 35 36 37 38 39
# 15

# time,hour,second = 0,0,0
# oxx
# xox
# xxo
# oox
# xoo
# oxo
# ooo 
# 15 45
# oxx
# oxo
# oox 
# ooo

# xxo
# xox 
# xoo



def solution():
    h=int(input())
    cnt=0
    for t in range(h+1):
        for m in range(60):
            for s in range(60):
                if '3' in str(s)+str(m)+str(t):
                    cnt+=1
    print(cnt)


        
solution()