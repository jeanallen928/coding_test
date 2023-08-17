"""
Programmers Lv.1(79%) # 12950 행렬의 덧셈
https://school.programmers.co.kr/learn/courses/30/lessons/12950

[문제 설명]
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

[제한 조건]
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

[입출력 예]
arr1	arr2	return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	[[3],[4]]	[[4],[6]]
"""
import numpy as np


arr11 = [[1, 2], [2, 3]]
arr12 = [[3, 4], [5, 6]]

arr21 = [[1], [2]]
arr22 = [[3], [4]]


def solution(arr1, arr2):

    np_arr1 = np.array(arr1)
    np_arr2 = np.array(arr2)

    return (np_arr1 + np_arr2).tolist()
# numpy 활용 답안. 코드 실행 통과 -----------------------------------------------


def solution(arr1, arr2):
    answer = []
    n = len(arr1)
    for i in range(n):
        answer.append([j+k for j, k in zip(arr1[i], arr2[i])])
    return answer
# 제출 답안: 1점! ----------------------------------------------------------


def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1
# 좋아요 43개, 17명 답안 -----------------------------------------------------


def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer
# 좋아요 101개, 35명 답안 ----------------------------------------------------


def solution(arr1, arr2):
    return [list(map(sum, zip(*x))) for x in zip(arr1, arr2)]
# 좋아요 89개 답안 ----------------------------------------------------------


print(solution(arr11, arr12))
print(solution(arr21, arr22))
