# programmers #181921 배열만들기 2
# 5	555	[5, 50, 55, 500, 505, 550, 555]
# 10	20	[-1]

from itertools import product


def solution(l, r):
    answer = []
    base = [0, 5]
    len_l, len_r = len(str(l)), len(str(r))

    all_data = []
    for i in range(len_l, len_r+1):
        all_data += list(product(base, repeat=i))
    for i in all_data:
        if i[0] != 0:
            check_ = int("".join(map(str, list(i))))
            if l <= check_ <= r:
                answer.append(check_)
    if len(answer) == 0:
        return [-1]
    else:
        return answer


print(solution(5, 555))
print(solution(10, 20))

# 코드 리뷰 이후 풀이 11점!!!-------------------------------------------------------------


# 준열님 코드-------------------------------------------------------------------------
def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if str(i).replace('5', '').replace('0', '') == '':
            answer.append(i)
    if answer == []:
        answer.append(-1)
    return answer


# 광운님 코드-------------------------------------------------------------------------
def solution(l, r):
    result = []
    num1 = l//5*5
    num2 = r//5*5 + 5
    for i in range(num1, num2, 5):
        if set(str(i)) == set({"0", "5"}) or set(str(i)) == set({'5'}):
            result.append(i)
    return result if result else [-1]
