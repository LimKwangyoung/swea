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
    while 0 <= pos[0] < N and 0 <= pos[1] < N:
        value = board[pos[0]][pos[1]]

        if pos == start or value == -1:
            return score
        if value == 5:
            return 2 * score + 1

        # wormhole
        if value >= 6:
            for coord in worm[value - 6]:
                if pos != coord:
                    pos = coord[:]
                    break
        # block
        elif value >= 1:
            new_direction = blocks[value - 1][direction]
            if abs(new_direction - direction) == 2:
                return 2 * score + 1
            direction = new_direction
            score += 1
        move()
    return 2 * score + 1


blocks = [[2, 3, 1, 0], [1, 3, 0, 2], [3, 2, 0, 1], [2, 0, 3, 1]]

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    board = []
    worm = [[] for _ in range(5)]
    for i in range(N):
        lst = list(map(int, input().split()))
        for j in range(N):
            if lst[j] >= 6:
                worm[lst[j] - 6].append([i, j])
        board.append(lst)

    result = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for k in range(4):
                    result = max(result, search([i, j], k))
    print(f'#{t} {result}')
