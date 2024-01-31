import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(5):
        result += board[i][i]
        result += board[i][N - 1 - i]
    if N % 2:
        result -= board[N // 2][N // 2]

    print(f'#{t} {result}')
