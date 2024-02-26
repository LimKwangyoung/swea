import sys

sys.stdin = open('input.txt')
##################################################


def covering(row: int, col: int, charger: int, coverage: int) -> None:
    for length, r in enumerate(range(row - coverage, row + 1)):
        for c in range(col - length, col + length + 1):
            if 1 <= r <= 10 and 1 <= c <= 10:
                if board[r][c] == [0]:
                    board[r][c] = [charger]
                else:
                    board[r][c].append(charger)
    for length, r in enumerate(range(row + 1, row + coverage + 1)):
        for c in range(col - (coverage - 1 - length), col + (coverage - 1 - length) + 1):
            if 1 <= r <= 10 and 1 <= c <= 10:
                if board[r][c] == [0]:
                    board[r][c] = [charger]
                else:
                    board[r][c].append(charger)


def move(pos: list, direction: str) -> list:
    if direction == '1':
        pos[1] -= 1
    elif direction == '2':
        pos[0] += 1
    elif direction == '3':
        pos[1] += 1
    elif direction == '4':
        pos[0] -= 1
    return pos


def charging(charger_1: list, charger_2: list) -> None:
    global result

    lst = []
    for num_1 in charger_1:
        for num_2 in charger_2:
            if num_1 == num_2:
                lst.append(chargers[num_1])
            else:
                lst.append(chargers[num_1] + chargers[num_2])
    result += max(lst)


T = int(input())

for t in range(1, T + 1):
    M, A = map(int, input().split())
    info_1, info_2 = input().split(), input().split()

    board = []
    for _ in range(11):
        board.append([[0] for _ in range(11)])
    chargers = {0: 0}
    for i in range(1, A + 1):
        X, Y, C, P = map(int, input().split())
        chargers[i] = P
        covering(X, Y, i, C)

    result = 0
    pos_1, pos_2 = [1, 1], [10, 10]
    charging(board[pos_1[0]][pos_1[1]], board[pos_2[0]][pos_2[1]])
    for i in range(M):
        pos_1 = move(pos_1, info_1[i])
        pos_2 = move(pos_2, info_2[i])
        charging(board[pos_1[0]][pos_1[1]], board[pos_2[0]][pos_2[1]])
    print(f'#{t} {result}')
