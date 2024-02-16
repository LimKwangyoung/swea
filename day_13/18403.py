import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections


def bfs(src: tuple) -> int:
    que = collections.deque([src])
    board[src[0]][src[1]] = 0
    while que:
        row, col = que.popleft()

        coord = ((row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1))
        for r, c in coord:
            if 0 <= r < N and 0 <= c < N and board[r][c] in ('0', '3'):
                if board[r][c] == '3':
                    return board[row][col]
                que.append((r, c))
                board[r][c] = board[row][col] + 1
    return 0


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    start = None
    for i in range(N):
        if start:
            break
        for j in range(N):
            if board[i][j] == '2':
                start = (i, j)

    print(f'#{t} {bfs(start)}')
