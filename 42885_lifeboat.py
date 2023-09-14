"""
Programmers Lv.2(%) # 42885 구명보트
https://school.programmers.co.kr/learn/courses/30/lessons/42885

[문제 설명]
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 
구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

[제한사항]
무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

[입출력 예]
people	limit	return
[70, 50, 80, 50]	100	3
[70, 80, 50]	100	3
"""
import math
from collections import deque

people1 = [70, 50, 80, 50]
limit1 = 100

people2 = [70, 80, 50]
limit2 = 100


def solution(people, limit):
    answer = 1
    people.sort()
    total = 0
    for kg in people:
        if total + kg < limit:
            total = total + kg
        elif total + kg == limit:
            answer += 1
            total = 0
        else:
            answer += 1
            total = kg
    return answer
# 코드 실행 통과, 정확성 테스트 1, 3 ~ 7, 9 ~ 13, 16 ~ 22 실패, 효율성 테스트 1 ~ 3 실패 ----


def solution(people, limit):
    answer = 0
    total = 0
    for i in range(len(people)):
        if min(people) > limit/2:
            return (answer + len(people))
        else:
            if total + min(people) < limit:
                total = total + min(people)
                people.remove(min(people))
            elif total + min(people) == limit:
                total = 0
                answer += 1
                people.remove(min(people))
            else:
                total = min(people)
                answer += 1
                people.remove(min(people))
    return answer


def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    for kg in people:
        if kg > limit/2:
            answer += 1
        elif kg > limit/3:
            answer += 0.5
        elif kg > limit/4:
            answer += 1/3
        elif kg > limit/5:
            answer += 0.25
        elif kg > limit/6:
            answer += 0.2
        else:
            answer += 1/6
    return math.ceil(answer)


def solution(people, limit):
    answer = 0
    total = 0
    people.sort()
    while len(people) > 0:
        try:
            total += people.pop()
            if total >= limit:
                answer += 1
                total = 0
            total += people.pop(0)
            if total >= limit:
                answer += 1
                total = 0
        except:
            print("error")
            break

    return answer, total


def solution(people, limit):
    answer = 0
    total = []
    people.sort()
    for i in range(len(people)):
        # while len(people) > 0:
        kg = people.pop()
        total.append(kg)
        if sum(total) >= limit:
            answer += 1
            total = []
        kg = people.pop(0)
        total.append(kg)
        if sum(total) >= limit:
            answer += 1
            total = []
    return answer, total


def solution(people, limit):
    answer = 0
    n = len(people)
    if n % 2 == 0:
        for i in range(1, int(n/2)+1):
            print(people[-i], people[i-1])
    else:
        for i in range(1, n//2+1):
            print(people[-i], people[i-1])
        print(people[n//2])
    return answer


def solution(people, limit):
    answer = 0
    people.sort()
    while len(people) > 1:
        if people[-1] + people[0] <= limit:
            answer += 1
            del people[-1], people[0]
        else:
            del people[-1]
            answer += 1
    if len(people) == 1:
        answer = answer + 1
    return answer
# 코드 실행 통과, 정황성 테스트 통과, 효율성 테스트 1 실패(시간 초과) ---------------------------


def solution(people, limit):
    answer = 0
    people.sort()
    while len(people) > 1:
        if people[-1] + people[0] <= limit:
            answer += 1
            people = people[1:-1]
        else:
            people.pop()
            answer += 1
    if len(people) == 1:
        answer = answer + 1
    return answer
# 코드 실행 통과, 정황성 테스트 통과, 효율성 테스트 1, 3 실패(시간 초과) ------------------------


# from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while len(people) > 1:
        if people[-1] + people[0] <= limit:
            answer += 1
            people.pop(), people.popleft()
        else:
            people.pop()
            answer += 1
    if len(people) == 1:
        answer = answer + 1
    return answer
# 제출 답안: 9점!!! --------------------------------------------------------


def solution(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1

    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
# 좋아요 60개, 352명 답안 ----------------------------------------------------


print(solution(people1, limit1))
print(solution(people2, limit2))
