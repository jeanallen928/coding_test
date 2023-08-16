"""
Programmers Lv.1(87%) # 12954 x만큼 간격이 있는 n개의 숫자 
https://school.programmers.co.kr/learn/courses/30/lessons/12954


[문제 설명]
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

[제한 조건]
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.

[입출력 예]
x	n	answer
2	5	[2,4,6,8,10]
4	3	[4,8,12]
-4	2	[-4, -8]
"""


x1 = 2
n1 = 5

x2 = 4
n2 = 3

x3 = -4
n3 = 2


def solution(x, n):
    if x < 0:
        answer = [i for i in range(x, x*n-1, x)]
    else:
        answer = [i for i in range(x, x*n+1, x)]
    return answer
# 테스트 8(x = 0) 실패. 런타임 에러 ---------------------------------------------


def solution(x, n):
    if x < 0:
        return [i for i in range(x, x*n-1, x)]
    elif x == 0:
        return [0 for i in range(n)]
    else:
        return [i for i in range(x, x*n+1, x)]
# 제출 답안: 5점!!! --------------------------------------------------------


def solution(x, n):
    return [i * x + x for i in range(n)]
# 좋아요 121개 답안 ---------------------------------------------------------


def solution(x, n):
    if x == 0:
        return [0 for i in range(n)]
    else:
        return [i for i in range(x, x*(n+1), x)]
# 끝값 개선 답안 ------------------------------------------------------------


print(solution(x1, n1))
print(solution(x2, n2))
print(solution(x3, n3))
