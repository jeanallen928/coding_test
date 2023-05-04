"""
달리기 경주
문제 설명
얀에서는 매년 달리기 경주가 열립니다. 
해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 
예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 
즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.


제한사항
5 ≤ players의 길이 ≤ 50,000
players[i]는 i번째 선수의 이름을 의미합니다.
players의 원소들은 알파벳 소문자로만 이루어져 있습니다.
players에는 중복된 값이 들어가 있지 않습니다.
3 ≤ players[i]의 길이 ≤ 10
2 ≤ callings의 길이 ≤ 1,000,000
callings는 players의 원소들로만 이루어져 있습니다.
경주 진행중 1등인 선수의 이름은 불리지 않습니다.
"""


players1 = ["mumu", "soe", "poe", "kai", "mine"]
callings1 = ["kai", "kai", "mine", "mine"]
# result1 = ["mumu", "kai", "mine", "soe", "poe"]

# index_result = [0, 3, 4, 1, 2]


# callings2 = ["mine", "kai", "kai", "mine"] == ["kai", "mine"]
# callings3 = ["mine", "kai", "poe", "mine"] == ["poe", "mine"]
# 엎치락 뒤치락 하면서 제자리로 돌아오는 경우를 빼서 for문을 줄여볼까 했지만 복잡


# players1 리스트의 요소를 key로, 인덱스를 value로 딕셔너리 만들기
# players_dictionary = {player: i for i, player in enumerate(players1)}
# {'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}

# 딕셔너리의 key와 value 스왑
# print({v: k for k, v in players_dictionary.items()})
# {0: 'mumu', 1: 'soe', 2: 'poe', 3: 'kai', 4: 'mine'}

# players1 리스트의 요소를 value로, 인덱스를 key로 딕셔너리 만들기
# dictionary = {i: players1[i] for i in range(len(players1))}
# {0: 'mumu', 1: 'soe', 2: 'poe', 3: 'kai', 4: 'mine'}


# print(players.index("kai"))
# original_index = players.index("kai")
# players.remove("kai")
# print(players)
# players.insert(original_index-1, "kai")
# print(players)
# print(players1)
# .index(), .remove(), .insert() 시간 복잡도 높아짐


# 테스트8까지 통과...-------------------------------------------------------------------
def solution(players, callings):
    for i in callings:
        original_index = players.index(i)
        players[original_index] = players[original_index-1]
        players[original_index-1] = i
    return players


def solution(players, callings):
    for i in callings:
        original_index = players.index(i)
        players[original_index], players[original_index -
                                         1] = players[original_index-1], players[original_index]
    return players
# 코드 실행 성공 / 정확성 테스트 8까지, 14-16 통과 / 나머지는 시간 초과로 실패------------------------------


def solution(players, callings):
    players_dictionary = {string: i for i, string in enumerate(players)}
    for i in callings:
        call_index = players_dictionary[i]  # 3
        players_dictionary[players[call_index-1]] += 1  # poe +1
        players_dictionary[i] -= 1  # kai -1
        players[call_index -
                1], players[call_index] = players[call_index], players[call_index-1]
    return players
# 제출 답안: 13점!!!------------------------------------------------------------------


def solution(players, callings):
    players_dict = {}
    for i, j in enumerate(players):
        players_dict[j] = i
    for i in callings:
        a = players_dict[i]
        cur = players[a]
        pre = players[a-1]
        players_dict[cur] -= 1
        players_dict[pre] += 1

        players[a] = players[a-1]
        players[a-1] = cur
    answer = players
    return answer
# 광운님 준열님 페어 코드------------------------------------------------------------------


print(solution(players1, callings1))
