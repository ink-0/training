def solution(arr1, arr2):
    answer = []
    for col in range(len(arr1)):
        answer.append([])
        for row in range(len(arr1[0])):
            answer[col].append(arr1[col][row]+arr2[col][row])

    return answer