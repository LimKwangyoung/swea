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
            cur = board[i][j]
            for k in range(1, cur + 1):
                coord = [(i - k, j), (i, j + k), (i + k, j), (i, j - k)]
                for r, c in coord:
                    if 0 <= r < N and 0 <= c < M:
                        cur += board[r][c]
            if cur > result:
                result = cur
    print(f'#{t} {result}')
