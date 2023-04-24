# programmers #120850 문자열 정렬하기 (1)

my_string1 = "hi12392"
# result = [1, 2, 2, 3, 9]
my_string2 = "p2o4i8gj2"
# result = [2, 2, 4, 8]
my_string3 = "abcde0"
# result = [0]


def solution(my_string):
    answer = []
    for string in my_string:
        if string.isdigit():
            answer.append(string)
    return list(map(int, sorted(answer)))


print(solution(my_string1))
print(solution(my_string2))
print(solution(my_string3))

# 준열님 코드-------------------------------------------------------------------------
# isnumeric으로 숫자인지 확인 후 맞으면 answer에 추가
answer = []
for i in my_string:
    if i.isnumeric():
        answer.append(int(i))
answer.sort()
print(answer)

# try - except로 풀면 어떨까?
answer = []
for i in my_string:
    try:
        answer.append(int(i))
    except:
        pass
answer.sort()
print(answer)


# 광운님 코드-------------------------------------------------------------------------
def solution(a):
    result = []
    for i in a:
        try:
            result.append(int(i))
        except ValueError:
            continue
    return sorted(result)


def solution(a):
    result = []
    for i in a:
        if i.isdigit():
            result.append(int(i))
    return sorted(result)


# 엘리사님 코드------------------------------------------------------------------------
def solution(my_string):
    answer = []
    for x in my_string:
        if x.isdigit():
            answer.append(int(x))
    return answer.sort()
