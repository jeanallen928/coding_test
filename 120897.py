# programmers #120897 약수 구하기

n1 = 24
# result1 = [1, 2, 3, 4, 6, 8, 12, 24]
n2 = 29
# result2 = [1, 29]

# n의 제곱근까지만 for문 반복--------------------------------------------------------------


def solution(n):
    answer = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            answer += [i, n//i]
    answer.sort()
    if int(n**0.5) == n**0.5:
        answer.remove(n**0.5)
    return answer
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------


def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return answer

# 제출 답안: 3점!!!-------------------------------------------------------------------


# 328명 답안------------------------------------------------------------------------
def solution(n):
    return [i for i in range(1, n+1) if n % i == 0]


print(solution(n1))
print(solution(n2))
