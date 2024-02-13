import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    for i in range(N):
        if board[-1][i] == '2':
            start = (N - 1, i)
            break

    stack = [start]
    while stack:
        row, col = stack.pop()
        if board[row][col] == '3':
            print(f'#{t} 1')
            break
        board[row][col] = '1'

        coord = ((row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1))
        for r, c in coord:
            if 0 <= r < N and 0 <= c < N and board[r][c] != '1':
                stack.append((r, c))
    else:
        print(f'#{t} 0')
