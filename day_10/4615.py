import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def conquer(center: tuple, delta: tuple) -> None:
    x, y = center
    dx, dy = delta

    x += dx
    y += dy
    lst = []

    while 0 <= x < N and 0 <= y < N:
        if board[x][y] == 0:
            return
        if board[x][y] == color:
            for x, y in lst:
                board[x][y] = color
            return
        lst.append((x, y))
        x += dx
        y += dy


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 2  # white
    board[N // 2][N // 2 - 1] = board[N // 2 - 1][N // 2] = 1  # black

    for _ in range(M):
        col, row, color = map(int, input().split())
        row -= 1
        col -= 1

        board[row][col] = color

        deltas = ((-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1))
        for dr, dc in deltas:
            if 0 <= row + dr < N and 0 <= col + dc < N and board[row + dr][col + dc] not in (0, color):
                conquer((row, col), (dr, dc))

    # counts of white and black
    black = white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print(f'#{t} {black} {white}')
