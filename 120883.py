# programmers #120883 로그인 성공?

id_pw1 = ["meosseugi", "1234"]
db1 = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]
# result = "login"

id_pw2 = ["programmer01", "15789"]
db2 = [["programmer02", "111111"], [
    "programmer00", "134"], ["programmer01", "1145"]]
# result = "wrong pw"

id_pw3 = ["rabbit04", "98761"]
db3 = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]
# result = "fail"


def solution(id_pw, db):
    ids = []
    pws = []
    for i in db:
        ids.append(i[0])
        pws.append(i[1])
    if id_pw[0] not in ids:
        answer = "fail"
    elif id_pw[1] != pws[ids.index(id_pw[0])]:
        answer = "wrong pw"
    else:
        answer = "login"
    return answer


print(solution(id_pw1, db1))
print(solution(id_pw2, db2))
print(solution(id_pw3, db3))


# 준열님 코드-------------------------------------------------------------------------
# 기본값을 fail로 주면 좋을듯
answer = 'fail'
# for 문으로 db안의 요소들을 검사
for i in db:
    if i[0] == id_pw[0]:
        if i[1] == id_pw[1]:
            answer = 'login'
            break
        else:
            answer = 'wrong pw'
            break


# 광운님 코드-------------------------------------------------------------------------
def solution(id_pw, db):
    if id_pw in db:
        return "login"
    for i in db:
        if i[0] in id_pw[0]:
            return "wrong pw"
        else:
            continue
    return "fail"
