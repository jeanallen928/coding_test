"""
Programmers # 120842 2차원으로 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/120842

[문제 설명]
정수 배열 num_list와 정수 n이 매개변수로 주어집니다. 
num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.

num_list가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 n이 2이므로 num_list를 2 * 4 배열로 다음과 같이 변경합니다. 
2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.


[제한사항]
num_list의 길이는 n의 배 수개입니다.
0 ≤ num_list의 길이 ≤ 150
2 ≤ n < num_list의 길이
"""

num_list1 = [1, 2, 3, 4, 5, 6, 7, 8]
num_list2 = [100, 95, 2, 4, 5, 6, 18, 33, 948]

n1 = 2
n2 = 3

result1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
result2 = [[100, 95, 2], [4, 5, 6], [18, 33, 948]]


def solution(num_list, n):
    answer = []
    for i in range(int(len(num_list)/n)):
        answer.append([num_list[:n]])
        del num_list[:n]
    return answer
# 제출 답안: 1점!!!-------------------------------------------------------------------


def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer
# 좋아요 20개 답안---------------------------------------------------------------------

print(solution(num_list1, n1))
print(solution(num_list2, n2))
