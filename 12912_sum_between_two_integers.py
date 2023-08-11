"""
Programmers Lv.1(55%) # 12912 두 정수 사이의 합 
https://school.programmers.co.kr/learn/courses/30/lessons/12912

[문제 설명]
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

[제한 조건]
a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
a와 b의 대소관계는 정해져있지 않습니다.

[입출력 예]
a	b	return
3	5	12
3	3	3
5	3	12
"""
a1 = 3
b1 = 5

a2 = 3
b2 = 3

a3 = 5
b3 = 3


def solution(a, b):
    input = [a, b]
    max_ = max(input)
    min_ = min(input)
    return ((max_-min_+1)*(max_+min_))/2
# 제출 답안: 2점! ----------------------------------------------------------


def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
# 23명, 좋아요 190개 답안 ----------------------------------------------------


def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2
# 좋아요 116개 답안 ---------------------------------------------------------


print(solution(a1, b1))
print(solution(a2, b2))
print(solution(a3, b3))
