import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [input().split() for _ in range(N)]

    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            # 90 degree
            print(board[N - 1 - j][i], end='')
        print(end=' ')
        for j in range(N):
            # 180 degree
            print(board[N - 1 - i][N - 1 - j], end='')
        print(end=' ')
        for j in range(N):
            # 270 degree
            print(board[j][N - 1 - i], end='')
        print()
