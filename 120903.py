# programmers #120903 배열의 유사도

s1_1 = ["a", "b", "c"]
s1_2 = ["com", "b", "d", "p", "c"]
# result1 = 2
s2_1 = ["n", "omg"]
s2_2 = ["m", "dot"]
# result2 = 0


def solution(s1, s2):
    answer = 0
    for i in s2:
        if i in s1:
            answer += 1
    return answer

# 제출 답안: 1점!!! + 광운님 코드----------------------------------------------------------


def solution(s1, s2):
    return len(set(s1) & set(s2))

# 좋아요 88개/300명 답안 + 준열님 코드-------------------------------------------------------


# 엘리사님 코드------------------------------------------------------------------------
def solution(s1, s2):
    s3 = s1 + s2
    answer = len(s3) - len(set(s3))
    return answer


print(solution(s1_1, s1_2))
print(solution(s2_1, s2_2))
