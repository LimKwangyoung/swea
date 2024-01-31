import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            total = 0
            for i in range(M):
                for j in range(M):
                    total += board[r + i][c + j]

            if result < total:
                result = total
    print(f'#{t} {result}')
