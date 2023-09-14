"""
Programmers Lv.2(79%) # 12939 최댓값과 최솟값
https://school.programmers.co.kr/learn/courses/30/lessons/12939

[문제 설명]
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를 들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

[제한 조건]
s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.

[입출력 예]
s	return
"1 2 3 4"	"1 4"
"-1 -2 -3 -4"	"-4 -1"
"-1 -1"	"-1 -1"
"""


s1 = "1 2 3 4"
s2 = "-1 -2 -3 -4"
s3 = "-1 -1"


def solution(s):
    list_ = s.split(' ')
    list_int = [int(i) for i in list_]
    return f"{min(list_int)} {max(list_int)}"
# 제출 답안: 1점! ----------------------------------------------------------


def solution(s):
    s = list(map(int, s.split()))
    return f"{min(s)} {max(s)}"
# 좋아요 63개, 520명 답안 + 나의 풀이 --------------------------------------------


print(solution(s1))
print(solution(s2))
print(solution(s3))
