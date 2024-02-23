import sys

sys.stdin = open(f'input.txt')
##################################################


def search(start: list, direction: int) -> int:
    def move() -> None:
        if direction == 0:
            pos[0] -= 1
        elif direction == 1:
            pos[1] += 1
        elif direction == 2:
            pos[0] += 1
        else:
            pos[1] -= 1

    score = 0

    pos = start[:]
    move()
    while 0 <= pos[0] < N and 0 <= pos[1] < N and pos != start and board[pos[0]][pos[1]] != -1:
        value = board[pos[0]][pos[1]]
        if value >= 6:
            for coord in worm[value - 6]:
                if pos != coord:
                    pos = coord[:]
                    break
        elif value == 5:
            return 2 * score + 1
        elif value >= 1:
            new_direction = blocks[value - 1][direction]
            if abs(new_direction - direction) == 2:
                return 2 * score + 1
            direction = new_direction
            score += 1
        move()

    if not (0 <= pos[0] < N and 0 <= pos[1] < N):
        score = 2 * score + 1
    return score


blocks = [[2, 3, 1, 0], [1, 3, 0, 2], [3, 2, 0, 1], [2, 0, 3, 1], [2, 3, 0, 1]]

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    worm = [[] for _ in range(5)]
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 6:
                worm[board[i][j] - 6].append([i, j])

    result = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for k in range(4):
                    result = max(result, search([i, j], k))
    print(f'#{t} {result}')
