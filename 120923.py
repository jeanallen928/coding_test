"""
programmers #120923 연속된 수의 합
https://school.programmers.co.kr/learn/courses/30/lessons/120923

[문제 설명]
연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 
두 정수 num과 total이 주어집니다. 
연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

[제한사항]
1 ≤ num ≤ 100
0 ≤ total ≤ 1000
num개의 연속된 수를 더하여 total이 될 수 없는 테스트 케이스는 없습니다.

"""


num1 = 3
total1 = 12
# result1 = [3, 4, 5]
1+2+3
num2 = 5
total2 = 15
# result2 = [1, 2, 3, 4, 5]
1+2+3+4+5
num3 = 4
total3 = 14
# result3 = [2, 3, 4, 5]
# 1+2+3+4=10
print((total3 - sum(range(1, num3+1)))//num3)
num4 = 5
total4 = 5
# result4 = [-1, 0, 1, 2, 3]
1+2+3+4+5


def solution(num, total):
    moves = (total - sum(range(1, num+1)))//num
    return [i for i in range(1+moves, num+1+moves)]
# 제출 답안: 8점!!!-------------------------------------------------------------------


def solution(num, total):
    middle_num = total//num
    if num % 2 == 1:
        answer = [i for i in range(
            middle_num - num//2, middle_num + num//2 + 1)]
    else:
        answer = [i for i in range(
            middle_num - num//2+1, middle_num + num//2 + 1)]
    return answer
# 광운님 준열님 페어 코드------------------------------------------------------------------


print(solution(num1, total1))
print(solution(num2, total2))
print(solution(num3, total3))
print(solution(num4, total4))
