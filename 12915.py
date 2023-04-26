# programmers #12915 문자열 내 마음대로 정렬하기

strings1 = ["sun", "bed", "car"]
n1 = 1
# return1 = ["car", "bed", "sun"]
strings2 = ["abce", "abcd", "cdx"]
n2 = 2
# return2 = ["abcd", "abce", "cdx"]


def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

# 제출 답안: 9점!!!-------------------------------------------------------------------


# 준열님 코드-------------------------------------------------------------------------
# 제출용 함수
def solution(strings, n):
    arr = [[string[n], string] for string in strings]
    arr.sort()
    answer = [i[1] for i in arr]
    return answer

# 한줄로 가능?


def solution2(strings, n):
    return [i[1] for i in sorted([[string[n], string] for string in strings])]


# 광운님 코드-------------------------------------------------------------------------
def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x: x[n])
    return strings


print(solution(strings1, n1))
print(solution(strings2, n2))
