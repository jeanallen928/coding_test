# programmers #68935 3진법 뒤집기

n1 = 45
# result1 = 7
n2 = 125
# result2 = 229


def solution(n):
    base3_list = []
    while n > 0:
        n, r = divmod(n, 3)
        base3_list.insert(0, r)
    base3 = "".join(map(str, base3_list))
    reverse_base3 = int(str(base3)[::-1])
    answer = int(str(reverse_base3), 3)
    return answer

# 제출 답안: 4점!!!-------------------------------------------------------------------


def solution(n):
    reverse_base3 = ''
    while n > 0:
        n, r = divmod(n, 3)
        reverse_base3 += str(r)
    return int(reverse_base3, 3)

# '다른 사람의 풀이' 본 후 개선 답안----------------------------------------------------------


# 준열님 코드-------------------------------------------------------------------------
# 재귀함수로 10진법 > 3진법 후 리버스
def dec_to_tri_reversed(number, str_tri=''):
    if number == 0:
        return str_tri
    return dec_to_tri_reversed(number//3, str_tri+str(number % 3))

# 재귀함수로 3진법 > 10진법


def tri_to_dec(str_tri, number=0, idx=0):
    if idx == len(str_tri):
        return number
    return tri_to_dec(str_tri, number+(3**idx)*int(str_tri[len(str_tri)-idx-1]), idx+1)

# 제출용 함수


def solution(n):
    answer = tri_to_dec(dec_to_tri_reversed(n), number=0, idx=0)
    return answer


# 광운님 코드-------------------------------------------------------------------------
def solution(n):
    a = n
    b = []
    answer = 0

    while a >= 1:
        b.append(a % 3)
        a = a // 3

    for i in range(len(b)):
        answer += b[i] * (3 ** (len(b) - i - 1))
    return answer


print(solution(n1))
print(solution(n2))
