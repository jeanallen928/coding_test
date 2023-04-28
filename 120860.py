# programmers #120860 직사각형 넓이 구하기 https://school.programmers.co.kr/learn/courses/30/lessons/120860


dots1 = [[1, 1], [2, 1], [2, 2], [1, 2]]
# result1 = 1
dots2 = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
# result2 = 4


def solution(dots):
    xs = []
    ys = []
    for i in dots:
        xs.append(i[0])
        ys.append(i[1])
    return (max(xs)-min(xs))*(max(ys)-min(ys))
# 제출답안: 6점!!!--------------------------------------------------------------------


# 다른 사람의 풀이:
    # xs = []
    # ys = []
    # -> xs, ys = [], []  이렇게 한 줄로 쓸 수 있다!


def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
# 좋아요 30개 / 23명 풀이---------------------------------------------------------------


print(solution(dots1))
print(solution(dots2))
