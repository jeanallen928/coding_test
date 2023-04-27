# programmers #120911 문자열 정렬하기 (2)

my_string1 = "Bcad"
result1 = "abcd"
my_string2 = "heLLo"
result2 = "ehllo"
my_string3 = "Python"
result3 = "hnopty"


def solution(my_string):
    answer = sorted(my_string.lower())
    return "".join(answer)


print(solution(my_string1))
print(solution(my_string2))
print(solution(my_string3))
