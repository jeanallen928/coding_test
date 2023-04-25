# programmers #120895 인덱스 바꾸기

my_string1 = "hello"
num1_1 = 1
num1_2 = 2
# result1 = "hlelo"
my_string2 = "I love you"
num2_1 = 3
num2_2 = 6
# result2 = "I l veoyou"


def solution(my_string, num1, num2):
    string_list = list(my_string)
    string_list[num1] = my_string[num2]
    string_list[num2] = my_string[num1]
    return "".join(string_list)


print(solution(my_string1, num1_1, num1_2))
print(solution(my_string2, num2_1, num2_2))


# 준열님 코드-------------------------------------------------------------------------
def solution(my_string, num1, num2):
    answer = ''
    for idx in range(len(my_string)):
        if idx == num1:
            idx = num2
        elif idx == num2:
            idx = num1
        answer += my_string[idx]
    return answer


# 광운님 코드-------------------------------------------------------------------------
def solution(my_string, num1, num2):
    a = my_string[num1]
    b = my_string[num2]
    c = num1
    d = num2
    new_string = my_string[:c] + b + my_string[c+1:d] + a + my_string[d+1:]

    return new_string


# 엘리사님 코드------------------------------------------------------------------------
def solution(my_string, num1, num2):
    answer = list(my_string)
    answer[num1], answer[num2] = answer[num2], answer[num1]
    return ''.join(answer)
