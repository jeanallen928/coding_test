# programmers #120904 숫자 찾기


num1 = 29183
k1 = 1
# result1 = 3
num2 = 232443
k2 = 4
# result2 = 4
num3 = 123456
k3 = 7
# result3 = -1


def solution(num, k):
    answer = str(num).find(str(k))
    return answer + 1 if answer != -1 else -1


print(solution(num1, k1))
print(solution(num2, k2))
print(solution(num3, k3))
