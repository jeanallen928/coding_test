# programmers #42748 K번째 수

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
result = [5, 6, 3]


def solution(array, commands):
    answer = []
    for i in commands:
        sliced = sorted(array[i[0]-1:i[1]])
        answer.append(sliced[i[2]-1])
    return answer


# i, j, k 한번에 쓰기-----------------------------------------------------------------
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer


# 좋아요 565개 / 151명 답안-------------------------------------------------------------
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


print(solution(array, commands))
