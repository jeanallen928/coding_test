# programmers #181895 배열 만들기 3

arr1 = [1, 2, 3, 4, 5]
intervals1 = [[1, 3], [0, 4]]
# result1 = [2, 3, 4, 1, 2, 3, 4, 5]


def solution(arr, intervals):
    answer = []
    for i in intervals:
        answer += arr[i[0]:i[1]+1]
    return answer

# 제출 답안: 5점!!! + 준열님 코드----------------------------------------------------------


# 광운님 코드-------------------------------------------------------------------------
def solution(arr, intervals):
    a = arr[intervals[0][0]:intervals[0][1]+1]
    b = arr[intervals[1][0]:intervals[1][1]+1]
    return a + b


print(solution(arr1, intervals1))
