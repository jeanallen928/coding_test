"""
Programmers Lv.2(74%) # 12924 숫자의 표현
https://school.programmers.co.kr/learn/courses/30/lessons/12924


[문제 설명]
Finn은 요즘 수학공부에 빠져 있습니다. 
수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 
예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

[제한사항]
n은 10,000 이하의 자연수 입니다.

[입출력 예]
n	result
15	4

[입출력 예 설명]
입출력 예#1
문제의 예시와 같습니다.
"""


n = 15
n1 = 1


def solution(n):
    answer = 1
    if n == 1:
        return 1   # n = 1인 경우(테스트 15)
    if n % 2 != 0:
        answer += 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            answer += 1
    return answer
# 정확성 테스트 1 ~ 3, 7, 8, 13 실패, 효율성 테스트 3 실패 ---------------------------


def solution(n):
    answer = 1
    for i in range(1, n // 2 + 1):
        m = 0
        sum = 0
        while sum < n:
            sum = sum + i + m
            m += 1
        if sum == n:
            answer += 1
    return answer
# 제출 답안: 7점!!! --------------------------------------------------------


def solution(n):
    return len([i for i in range(1, n+1, 2) if n % i == 0])
# 좋아요 52개 답안 ----------------------------------------------------------


print(solution(n))
print(solution(n1))
