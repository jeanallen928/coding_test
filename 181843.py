# programmers #181843 부분문자열인지 확인하기

my_string = "banana"
target1 = "ana"  # result: 1
target2 = "wxyz"  # result: 0


def solution(my_string, target):
    answer = 1
    if my_string.find(target) == -1:
        answer = 0
    return answer


print(solution(my_string, target1))
print(solution(my_string, target2))

# 준열님 코드-------------------------------------------------------------------------
# find로 풀기
if my_string.find(target) >= 0:
    answer = 1
else:
    answer = 0
print(answer)

# index로 풀기
try:
    my_string.index(target)
    answer = 1
except:
    answer = 0
print(answer)

# for로 풀기
answer = 0
for i in range(len(my_string)-len(target)+1):
    if my_string[i:i+len(target)] == target:
        answer = 1
        break
print(answer)


# 엘리사님 코드------------------------------------------------------------------------
def solution(my_string, target):
    string = my_string.find(target)
    if string == -1:
        answer = 0
    else:
        answer = 1
    return answer


# 광운님 코드-------------------------------------------------------------------------
def solution(my_string, target):
    return 1 if target in my_string else 0


def solution(my_string, target):
    return int(target in my_string)
