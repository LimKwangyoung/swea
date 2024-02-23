import sys

sys.stdin = open(f'input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    worm = [[] for _ in range(5)]
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 6:
                worm[board[i][j] - 6].append((i, j))
    print(worm)