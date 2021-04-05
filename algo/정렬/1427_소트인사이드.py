# inp_arr = input()
# ans=[]
# for i in inp_arr:
#     ans.append(i)
# ans.sort(reverse=True)

# ans="".join(ans)
# print(ans)

inp_arr = list(input())
inp_arr.sort(key=int , reverse=True)
print(inp_arr)
print(''.join(inp_arr))