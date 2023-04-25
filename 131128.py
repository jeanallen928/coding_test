# programmers #131128 숫자 짝꿍

from collections import Counter
"100"	"2345"	"-1"
"100"	"203045"	"0"
"100"	"123450"	"10"
"12321"	"42531"	"321"
"5525"	"1255"	"552"


def solution(X, Y):
    repeat_num = []
    if len(set(X).intersection(set(Y))) == 0:
        return "-1"
    elif set(X).intersection(set(Y)) == {"0"}:
        return "0"
    else:
        for i in Y:
            if X.find(i) != -1:
                repeat_num.append(i)
        return str("".join(sorted(repeat_num, reverse=True)))


# 정확성 테스트3, 5, 8, 10-15 실패 / 52.6점 ##############################################


# print(solution("100", "2345"))
# print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))

# print("100".find("2345"))
# print("100".find("203045"))  # -1
# for i in "203045":
#     print("100".find(i))
# print(set("100"))
# print(set("100").intersection(set("203045")))
# repeat_num = sorted(
#     list(set(X).intersection(set(Y))), reverse=True)

"100", "123450", "10"

# print("100".count("0"))


def solution(X, Y):
    repeat_num = []
    for i in Y:
        if X.find(i) != -1:
            repeat_num.append(i)
    if len(repeat_num) == 0:
        return "-1"
    elif set(repeat_num) == {"0"}:
        return "0"
    else:
        return str("".join(sorted(repeat_num, reverse=True)))

# 정확성 테스트3, 5, 8, 10-15 실패 / 52.6점 ##############################################


# print("100".count("0"))
# print("123450".count("0"))
# print(set("123450"))
# for i in set("123450"):
#     print("100".find(i))


# 준열님 코드-------------------------------------------------------------------------
def solution(X, Y):
    answer = ''
    arr_x = [0]*10
    arr_y = [0]*10
    for i in X:
        arr_x[int(i)] += 1
    for i in Y:
        arr_y[int(i)] += 1
    for i in range(0, 10):
        answer = str(i)*(min(arr_x[i], arr_y[i])) + answer
    if answer == '':
        answer = '-1'
    elif answer.replace('0', '') == '':
        answer = '0'
    return answer


# 광운님 코드-------------------------------------------------------------------------
# from collections import Counter

def solution(X, Y):
    intersection = list((Counter(X) & Counter(Y)).elements())
    intersection.sort(reverse=True)

    a = "".join(sorted(intersection, reverse=True))
    if set(a) == {"0"}:
        return "0"
    elif a == "":
        return "-1"
    else:
        return a


# 코드 리뷰 후 개선하기!------------------------------------------------------------------
# from collections import Counter

def solution(X, Y):
    inter_ = set(X).intersection(set(Y))
    if len(inter_) == 0:
        return "-1"
    elif inter_ == {"0"}:
        return "0"
    else:
        intersection = list((Counter(X) & Counter(Y)).elements())
        return "".join(sorted(intersection, reverse=True))

# 18점!!! ########################################################################
