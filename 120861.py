# programmers #120861 캐릭터의 좌표

keyinput1 = ["left", "right", "up", "right", "right"]
board1 = [11, 11]
board_m1 = list(map(lambda x: (x-1)/2, board1))
print(board_m1)
# result1 = [2, 1]
keyinput2 = ["down", "down", "down", "down", "down"]
board2 = [7, 9]
board_m2 = list(map(lambda x: (x-1)/2, board2))
print(board_m2)
# result2 = [0, -4]


def solution(keyinput, board):
    answer = [0, 0]
    board_m = list(map(lambda x: (x-1)/2, board))
    x_ = keyinput.count("right")-keyinput.count("left")
    y_ = keyinput.count("up")-keyinput.count("down")
    if abs(x_) < board_m[0]:
        answer[0] = x_
    elif x_ < 0:
        answer[0] = -board_m[0]
    else:
        answer[0] = board_m[0]
    if abs(y_) < board_m[1]:
        answer[1] = y_
    elif y_ < 0:
        answer[1] = -board_m[1]
    else:
        answer[1] = board_m[1]
    return answer


# 정확성 테스트8 실패 / 90.9점 ###########################################################


# 준열님 코드-------------------------------------------------------------------------
def solution(keyinput, board):
    board_width = board[0]//2
    board_hight = board[1]//2

    keyinput_dic = {"up": [0, 1], "down": [
        0, -1], "left": [-1, 0], "right": [1, 0]}
    answer = [0, 0]
    for i in keyinput:
        if board_width >= answer[0]+keyinput_dic[i][0] >= -board_width:
            answer[0] += keyinput_dic[i][0]
        if board_hight >= answer[1]+keyinput_dic[i][1] >= -board_hight:
            answer[1] += keyinput_dic[i][1]
    return answer


# 광운님 코드-------------------------------------------------------------------------
def solution(keyinput, board):
    position = [0, 0]
    for direction in keyinput:
        if direction == "right":
            if position[0] == board[0]//2:
                pass
            else:
                position[0] += 1

        elif direction == "left":
            if position[0] == -board[0]//2+1:
                pass
            else:
                position[0] -= 1

        elif direction == "up":
            if position[1] == board[1]//2:
                pass
            else:
                position[1] += 1

        elif direction == "down":
            if position[1] == -board[1]//2+1:
                pass
            else:
                position[1] -= 1
    return position

# 광운님 개선 코드----------------------------------------------------------------------


def solution(keyinput, board):
    position = [0, 0]
    x, y = 0, 0
    for direction in keyinput:
        if direction == "right":
            x = min(x + 1, board[0]//2)
        if direction == "left":
            ...
    return [x, y]


# 코드 리뷰 후 개선하기!------------------------------------------------------------------
def solution(keyinput, board):
    answer = [0, 0]
    board_m = list(map(lambda x: (x-1)/2, board))
    for i in keyinput:
        if i == "left":
            answer[0] = max(answer[0]-1, -board_m[0])
        elif i == "right":
            answer[0] = min(answer[0]+1, board_m[0])
        elif i == "up":
            answer[1] = min(answer[1]+1, board_m[1])
        else:
            answer[1] = max(answer[1]-1, -board_m[1])
    return answer

# 12점!!! ########################################################################
