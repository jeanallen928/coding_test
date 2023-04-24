# programmers #120876 겹치는 선분의 길이


import numpy as np

lines1 = [[0, 1], [2, 5], [3, 9]]  # 2
lines2 = [[-1, 1], [1, 3], [3, 9]]  # 0
lines3 = [[0, 5], [3, 9], [1, 10]]  # 8


def solution(lines):
    modified = []
    for i in lines:
        modified.append(list(np.arange(i[0]+0.5, i[1], 1)))

    intersect1 = set(modified[0]) & set(modified[1])
    intersect2 = set(modified[1]) & set(modified[2])
    intersect3 = set(modified[2]) & set(modified[0])

    union_ = intersect1 | intersect2 | intersect3

    return len(union_)


print(solution(lines1))
print(solution(lines2))
print(solution(lines3))


# 준열님 코드-------------------------------------------------------------------------
answer = 0
# 직선의 중심인 x.5를 지나는 선이 여러개면 겹치는 부분임
# 리스트에다가 x.5를 구해서 다 집어넣자
arr = []
for i in lines:
    for j in range(i[0], i[1]):
        arr.append(j+0.5)
print(arr)
# arr의 중복제거를 위해 set으로 만들고
# for문으로 count해서 1이 아니면 answer를 1씩 늘림
for i in set(arr):
    if arr.count(i) != 1:
        answer += 1
print(answer)
