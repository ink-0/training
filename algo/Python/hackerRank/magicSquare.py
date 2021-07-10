# def formingMagicSquare(s):
#     # Write your code here\
#      magic1 = [[4,9,2],[3,5,7],[8,1,6]]
#      magic11 = [[2,9,4],[7,5,3],[6,1,8]]

#      magic2 = [[2,7,6],[9,5,1],[4,3,8]]
#      magic22 = [[6,7,2],[1,5,9],[8,3,4]]

#      magic3 = [[6,1,8],[7,5,3],[2,9,4]]
#      magic33 = [[8,1,6],[3,5,7],[4,9,2]]

#      magic4 = [[8,3,4],[1,5,9],[6,7,2]]
#      magic44 = [[4,3,8],[9,5,1],[2,7,6]]

#      minCost=[0,0,0,0,0,0,0,0]
#      for i in range(3):

#         for j in range(3):
#             minCost[0]+=abs(s[i][j]-magic1[i][j])
#             minCost[1]+=abs(s[i][j]-magic11[i][j])

#             minCost[2]+=abs(s[i][j]-magic2[i][j])
#             minCost[3]+=abs(s[i][j]-magic22[i][j])

#             minCost[4]+=abs(s[i][j]-magic3[i][j])
#             minCost[5]+=abs(s[i][j]-magic33[i][j])

#             minCost[6]+=abs(s[i][j]-magic4[i][j])
#             minCost[7]+=abs(s[i][j]-magic44[i][j])



#      return min(minCost)
# print(formingMagicSquare([[4,5,8],[2,4,1],[1,9,7]]))
def formingMagicSquare(s):


    s = sum(s, [])
    print(s)

    ans = [[8, 1, 6, 3, 5, 7, 4, 9, 2]
    ,[6, 1, 8, 7, 5, 3, 2, 9, 4]
    ,[4, 3, 8, 9 ,5 ,1, 2, 7, 6]    
    ,[2, 7, 6, 9, 5, 1, 4, 3, 8]
    ,[2, 9, 4, 7, 5, 3, 6, 1, 8]
    ,[4, 9, 2, 3, 5, 7, 8, 1, 6]
    ,[6, 7, 2, 1, 5, 9, 8, 3, 4]
    ,[8, 3, 4, 1, 5, 9, 6, 7, 2]
    ]

    result = []
    sumval = 0
   
    # print(s)
    for i in range(8):
        for j in range(9):
            sumval += abs(s[j]-ans[i][j])
            print(i,j,'ij',s[j],ans[i][j])
        if sumval == 0:
            return 0  

        result.append(sumval)
        sumval = 0
        
    # print(result)    
    return min(result)
# print('단거')
print(formingMagicSquare([[4,5,8],[2,4,1],[1,9,7]]))

