"""
programmers #120905 n의 배수 고르기
https://school.programmers.co.kr/learn/courses/30/lessons/120905

[문제 설명]
정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

[제한사항]
1 ≤ n ≤ 10,000
1 ≤ numlist의 크기 ≤ 100
1 ≤ numlist의 원소 ≤ 100,000
"""

n1 = 3
n2 = 5
n3 = 12

numlist1 = [4, 5, 6, 7, 8, 9, 10, 11, 12]
numlist2 = [1, 9, 3, 10, 13, 5]
numlist3 = [2, 100, 120, 600, 12, 12]

result1 = [6, 9, 12]
result2 = [10, 5]
result3 = [120, 600, 12, 12]


def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer
# 제출 답안: 1점/ 봉글봉글 , 승우 , chobojajg , dlrtn75 외 1998 명----------------------------


def solution(n, numlist):
    return [i for i in numlist if i % n == 0]
# pgstter , 주뇽킴 , sexymonster , mmmik 외 226 명------------------------------------


print(solution(n1, numlist1))
print(solution(n2, numlist2))
print(solution(n3, numlist3))