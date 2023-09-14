"""
Programmers Lv.2(%) # 12909 올바른 괄호
https://school.programmers.co.kr/learn/courses/30/lessons/12909

[문제 설명]
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 
예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

[제한사항]
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

[입출력 예]
s	answer
"()()"	true
"(())()"	true
")()("	false
"(()("	false

[입출력 예 설명]
입출력 예 #1,2,3,4
문제의 예시와 같습니다.
"""


s1 = "()()"
s2 = "(())()"
s3 = ")()("
s4 = "(()("
s5 = "(()))()()"


def solution(s):
    while s.count("()") > 0:
        s_ = s.replace("()", '')
        s = s_
    return True if len(s_) == 0 else False
# 코드 실행 통과. 정확성 테스트: 테스트 1 ~ 3 런타임 에러 실패, 효율성 테스트: 테스트 1 ~ 2 시간 초과 실패 -


def solution(s):
    # answer = []
    # if s[0] == ")":
    #     return False
    # else:
    temp = []
    for i in s:
        if i == "(":
            temp.append(i)
        if i == ")":
            try:
                temp.pop()
            except:
                return False
    if len(temp) == 0:
        return True
    else:
        return False


def solution(s):
    temp = []
    for i in s:
        if i == "(":
            temp.append(i)
        elif i == ")":
            try:
                temp.pop()
            except:
                return False
    if len(temp) == 0:
        return True
    else:
        return False
# 제출 답안: 3점! ----------------------------------------------------------


def solution(s):
    temp = []
    for i in s:
        if i == "(":
            temp.append(i)
        elif i == ")":
            try:
                temp.pop()
            except:
                return False
    return len(temp) == 0
# 개선 답안 ---------------------------------------------------------------


print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))
