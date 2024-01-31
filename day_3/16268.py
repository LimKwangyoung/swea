import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            pollen = board[i][j]

            coord = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
            for r, c in coord:
                if 0 <= r < N and 0 <= c < M:
                    pollen += board[r][c]

            if result < pollen:
                result = pollen
    print(f'#{t} {result}')
