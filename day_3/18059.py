import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())

    board = [[0] * 10 for _ in range(10)]

    result = 0
    for _ in range(N):
        x1, y1, x2, y2, _ = map(int, input().split())
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if board[i][j]:
                    result += 1
                else:
                    board[i][j] = 1
    print(f'#{t} {result}')
