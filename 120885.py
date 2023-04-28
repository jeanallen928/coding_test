# programmers #120885 이진수 더하기

bin1_1 = "10"
bin1_2 = "11"
# result1 = "101"
bin2_1 = "1001"
bin2_2 = "1111"
# result2 = "11000"


def solution(bin1, bin2):
    sum = int(bin1, 2) + int(bin2, 2)
    answer = bin(sum)[2:]
    return answer
# 페어코딩! 제출 답안: 6점!!!-------------------------------------------------------------


print(solution(bin1_1, bin1_2))
print(solution(bin2_1, bin2_2))


# 재귀함수로 int(string,2) 만들어보기!
def bin_to_dec(string, n=0):
    if not string:
        return 0
    return int(string[-1])*(2**(n)) + bin_to_dec(string[:-1], n+1)


print(bin_to_dec("11000"))  # 24


# 재귀함수로 bin(num) 만들어보기!
def dec_to_bin(num):
    if num == 0:
        return ''
    return dec_to_bin(num//2) + str(num % 2)


print(dec_to_bin(10))  # 1010
