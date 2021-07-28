def solution():
    n = int(input())
    student = []
    for i in range(n):
        name,grade = input().split()
        student.append([name,int(grade)])
    student =sorted(student,key = lambda x : x[1] )
    for i in student:
        print(i[0],end=' ')
solution()