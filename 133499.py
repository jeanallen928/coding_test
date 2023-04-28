# programmers #133499 옹알이(2) https://school.programmers.co.kr/learn/courses/30/lessons/133499

# 머쓱이네 조카가 할 수 있는 말: "aya", "ye", "woo", "ma"
# 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다.
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ babbling의 길이 ≤ 100
# 1 ≤ babbling[i]의 길이 ≤ 30
# 문자열은 알파벳 소문자로만 이루어져 있습니다.

babbling1 = ["aya", "yee", "u", "maa"]
# result1 = 1
babbling2 = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
# result2 = 2


def solution(babbling):
    answer = 0
    return answer


def solution(babbling):
    answer = 0
    for idx, string in enumerate(babbling):
        babbling[idx] = string.replace('aya', '1').replace(
            'ye', '2').replace('woo', '3').replace('ma', '4')
        if babbling[idx].isdigit():
            if not ('11' in babbling[idx] or '22' in babbling[idx] or '33' in babbling[idx] or '44' in babbling[idx]):
                answer += 1
    return answer
# 페어코딩 답안------------------------------------------------------------------------


print(solution(babbling1))
print(solution(babbling2))
