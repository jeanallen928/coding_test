# programmers #12969 직사각형 별찍기

# 입력: 5 3
# 출력:
# *****
# *****
# *****

a, b = map(int, input().strip().split(' '))
for i in range(b):
    print("*"*a)


# 맨 마지막 줄 한 줄--------------------------------------------------------------------

a, b = map(int, input().strip().split(' '))
print(('*'*a + '\n')*b)

a, b = map(int, input().strip().split(' '))
print(('*'*a + '\n')*(b-1)+'*'*a)
