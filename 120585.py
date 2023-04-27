# programmers #120585 머쓱이보다 키 큰 사람

array1 = [149, 180, 192, 170]
height1 = 167
# result1 = 3
array2 = [180, 120, 140]
height2 = 190
# result2 = 0


def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer


print(solution(array1, height1))
print(solution(array2, height2))
