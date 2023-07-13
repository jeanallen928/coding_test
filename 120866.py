from numpy import array, where, count_nonzero
"""
Programmers 안전지대
https://school.programmers.co.kr/learn/courses/30/lessons/120866

[문제설명]
다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
image.png
지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

[제한사항]
board는 n * n 배열입니다.
1 ≤ n ≤ 100
지뢰는 1로 표시되어 있습니다.
board에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.

"""

# [입출력 예]
board1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
result1 = 16
board2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
result2 = 13
board3 = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
result3 = 0
board4 = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
result4 = 5

"""
입출력 예 설명
입출력 예 #1
(3, 2)에 지뢰가 있으므로 지뢰가 있는 지역과 지뢰와 인접한 위, 아래, 좌, 우, 대각선 총 8칸은 위험지역입니다. 따라서 16을 return합니다.

입출력 예 #2
(3, 2), (3, 3)에 지뢰가 있으므로 지뢰가 있는 지역과 지뢰와 인접한 위, 아래, 좌, 우, 대각선은 위험지역입니다. 따라서 위험지역을 제외한 칸 수 13을 return합니다.

입출력 예 #3
모든 지역에 지뢰가 있으므로 안전지역은 없습니다. 따라서 0을 return합니다.
"""


"""
1개: 16개 = 25 - 9 = 5 * 5 - 9
2개: 13개 = 25 - 12 = 5 * 5 - 12
25개: 0개 = 25 - 25 = 5 * 5 - 25
행렬로 해서 1인 것의 주변을 1로 바꿔주고 행렬 범위를 넘어가면 에러 그냥 넘어가게 try/except로 하면 되지 않을까?
행렬 numpy였나? 행렬을 검색해보자. -> numpy의 array
1로 바꿔버리면 기존 1과 구분이 안감.
슬라이싱으로 바꿔버리면 기존1도 바뀌어버림
"""


def solution(board):
    n = len(board)
    matrix = array(board)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                try:
                    if matrix[i-1, j+1] == 0:
                        matrix[i-1, j+1] = 2
                    if matrix[i-1, j] == 0:
                        matrix[i-1, j] = 2
                    if matrix[i-1, j-1] == 0:
                        matrix[i-1, j-1] = 2
                    if matrix[i, j-1] == 0:
                        matrix[i, j-1] = 2
                    if matrix[i, j+1] == 0:
                        matrix[i, j+1] = 2
                    if matrix[i+1, j+1] == 0:
                        matrix[i+1, j+1] = 2
                    if matrix[i+1, j] == 0:
                        matrix[i+1, j] = 2
                    if matrix[i+1, j-1] == 0:
                        matrix[i+1, j-1] = 2
                except:
                    pass

    answer = n * n - count_nonzero(matrix)
    return answer
# 코드 실행 pass. 제출 후 채점: 63.0 테스트 1, 4, 5, 7 fail ----------------------------------


def solution(board):
    n = len(board)
    matrix = array(board)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                try:
                    if matrix[i-1, j+1] == 0 and i - 1 >= 0:
                        matrix[i-1, j+1] = 2
                    if matrix[i-1, j] == 0 and i - 1 >= 0:
                        matrix[i-1, j] = 2
                    if matrix[i-1, j-1] == 0 and i - 1 >= 0 and j - 1 >= 0:
                        matrix[i-1, j-1] = 2
                    if matrix[i, j-1] == 0 and j - 1 >= 0:
                        matrix[i, j-1] = 2
                    if matrix[i, j+1] == 0:
                        matrix[i, j+1] = 2
                    if matrix[i+1, j+1] == 0:
                        matrix[i+1, j+1] = 2
                    if matrix[i+1, j] == 0:
                        matrix[i+1, j] = 2
                    if matrix[i+1, j-1] == 0 and j - 1 >= 0:
                        matrix[i+1, j-1] = 2
                except:
                    pass

    answer = n * n - count_nonzero(matrix)
    return answer
# 코드 실행 pass. 제출 후 채점: 72.2 테스트 4, 5, 7 fail ----------------------------------


def solution(board):
    n = len(board)
    matrix = array(board)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:

                if i - 1 >= 0 and j + 1 <= n - 1 and matrix[i-1, j+1] == 0:
                    matrix[i-1, j+1] = 2
                if i - 1 >= 0 and matrix[i-1, j] == 0:
                    matrix[i-1, j] = 2
                if i - 1 >= 0 and j - 1 >= 0 and matrix[i-1, j-1] == 0:
                    matrix[i-1, j-1] = 2
                if j - 1 >= 0 and matrix[i, j-1] == 0:
                    matrix[i, j-1] = 2
                if j + 1 <= n - 1 and matrix[i, j+1] == 0:
                    matrix[i, j+1] = 2
                if j + 1 <= n - 1 and i + 1 <= n - 1 and matrix[i+1, j+1] == 0:
                    matrix[i+1, j+1] = 2
                if i + 1 <= n - 1 and matrix[i+1, j] == 0:
                    matrix[i+1, j] = 2
                if j - 1 >= 0 and i + 1 <= n - 1 and matrix[i+1, j-1] == 0:
                    matrix[i+1, j-1] = 2

    answer = n * n - count_nonzero(matrix)
    return answer
# 제출 답안: 8점!!! ------------------------------------------------------------------


print(solution(board1))
print(solution(board2))
print(solution(board3))
print(solution(board4))


# from numpy import array, where, count_nonzero
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj)
                          for di in [-1, 0, 1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)
# 좋아요 39개, 15명 답안 ---------------------------------------------------------------
