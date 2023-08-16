"""
Programmers Lv.1(80%) # 12918 문자열 다루기 기본
https://school.programmers.co.kr/learn/courses/30/lessons/12918


[문제 설명]
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

[제한 사항]
s는 길이 1 이상, 길이 8 이하인 문자열입니다.
s는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.

[입출력 예]
s	return
"a234"	false
"1234"	true
"""


s1 = "a234"
s2 = "1234"


def solution(s):
    return s.isdigit()
# 테스트 5, 6, 28, 29 실패 -------------------------------------------------


def solution(s):
    return s.isdecimal()
# 테스트 5, 6, 28, 29 실패 -------------------------------------------------


# 문제 설명에서 "문자열 s의 길이가 4 혹은 6이고, ......" is가 아니라 and


def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        answer = s.isdigit()
    return answer
# 제출 답안: 9점!!! --------------------------------------------------------


def solution(s):
    return s.isdigit() and len(s) in [4, 6]
# 좋아요 188개, 66명 답안 ----------------------------------------------------


def solution(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6
# 좋아요 59개 답안 ----------------------------------------------------------


print(solution(s1))
print(solution(s2))
