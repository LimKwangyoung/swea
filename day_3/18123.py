import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            coord = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
            for r, c in coord:
                if 0 <= r < N and 0 <= c < N:
                    result += abs(board[i][j] - board[r][c])
    print(f'#{t} {result}')
