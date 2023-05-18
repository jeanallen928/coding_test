"""
주사위 게임 3
문제 설명
1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

제한사항
a, b, c, d는 1 이상 6 이하의 정수입니다.

입출력 예
a	b	c	d	result
2	2	2	2	2222
4	1	4	4	1681
6	3	3	6	27
2	5	2	6	30
6	4	2	5	2

"""

def solution(a, b, c, d):
    num = [a, b, c, d]
    uniq_list = list(set(num))
    
    if len(uniq_list)==1:  # 모두 같은 숫자
        return 1111*a
    
    elif len(uniq_list)==4:  # 모두 다른 숫자
        return min(num)
    
    elif len(uniq_list)==3:  # 2개 같고 나머지는 다른 숫자
        uniq_uniq = []
        for i in uniq_list:
            if num.count(i) == 1:
                uniq_uniq.append(i)
        return uniq_uniq[0]*uniq_uniq[1]
    
    elif len(uniq_list)==2:  # 2개 2개 또는 3개 1개

        for index_i, num_i in enumerate(uniq_list):
            
            if num.count(num_i) == 3:  # 3개 1개
                repeat_num = uniq_list.pop(index_i)
                return (repeat_num*10+uniq_list[0])**2
            elif num.count(num_i) == 2:  # 2개 2개
                p = list(set(num))[0]
                q = list(set(num))[1]
                return (p + q) * abs(p - q)
        
# 제출 답안: 8점!!!-------------------------------------------------------------------

print(solution(2, 2, 2, 2))
print(solution(4, 1, 4, 4))
print(solution(6, 3, 3, 6))
print(solution(2, 5, 2, 6))
print(solution(6, 4, 2, 5))
