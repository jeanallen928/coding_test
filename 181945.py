'''
programmers #181945 문자열 돌리기
https://school.programmers.co.kr/learn/courses/30/lessons/181945

문제 설명
문자열 str이 주어집니다.
문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.

제한사항
1 ≤ str의 길이 ≤ 10

'''

# str = abcde
# # result
# # a
# # b
# # c
# # d
# # e

str = input()
for s in str:
    print(s)
# 제출 답안: 1점----------------------------------------------------------------------

str = input()
print("\n".join(list(str)))
# 엘리사님 코드------------------------------------------------------------------------
