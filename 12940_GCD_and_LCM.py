"""
Programmers Lv.1(77%) # 12940 최대공약수와 최소공배수
https://school.programmers.co.kr/learn/courses/30/lessons/12940

[문제 설명]
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

[제한 사항]
두 수는 1이상 1000000이하의 자연수입니다.

[입출력 예]
n	m	return
3	12	[3, 12]
2	5	[1, 10]

[입출력 예 설명]
입출력 예 #1
위의 설명과 같습니다.

입출력 예 #2
자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.
"""
import math


n1 = 3
m1 = 12

n2 = 2
m2 = 5


def solution(n, m):
    return [math.gcd(n, m), math.lcm(n, m)]
# lcm() python 3.9 부터! ------------------------------------------------


def solution(n, m):
    gcd = math.gcd(n, m)
    return [gcd, n*m/gcd]
# 코드 리뷰 후 개선 ----------------------------------------------------------


def solution(n, m):
    a = max(n, m)
    b = min(n, m)
    x = a*b
    while a % b > 0:
        b = a % b
    return [b, x/b]
# 코드 실행 통과, 테스트 2, 12, 16 실패 ------------------------------------------


def solution(n, m):
    a = max(n, m)
    b = min(n, m)
    x = a*b
    while a % b > 0:
        r = a % b
        a = b
        b = r
    return [b, x/b]
# 제출 답안: 4점! ----------------------------------------------------------


def solution(n, m):
    x = n*m
    while n % m > 0:
        r = n % m
        n = m
        m = r
    return [m, x/m]
# 코드 리뷰 후 개선 ----------------------------------------------------------


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def lcm(a, b):
    return int(a * b / gcd(a, b))


def gcdlcm(a, b):
    answer = [gcd(a, b), lcm(a, b)]
    return answer
# 좋아요 10개, 재귀함수 사용 답안 -------------------------------------------------


print(solution(n1, m1))
print(solution(n2, m2))


print(gcdlcm(n1, m1))
print(gcdlcm(n2, m2))
