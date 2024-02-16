import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections


def dfs(src: tuple) -> int:
    stack = [src]
    while stack:
        row, col = stack.pop()
        if board[row][col] == '3':
            return 1
        if board[row][col] != '1':
            board[row][col] = '1'
            coord = ((row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1))
            for r, c in coord:
                if 0 <= r < 100 and 0 <= c < 100:
                    stack.append((r, c))
    return 0


def bfs(src: tuple) -> int:
    que = collections.deque([src])
    board[src[0]][src[1]] = '1'
    while que:
        row, col = que.popleft()
        coord = ((row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1))
        for r, c in coord:
            if 0 <= r < 100 and 0 <= c < 100 and board[r][c] != '1':
                if board[r][c] == '3':
                    return 1
                que.append((r, c))
                board[r][c] = '1'
    return 0


for _ in range(10):
    t = int(input())
    board = [list(input()) for _ in range(100)]

    start = None
    for i in range(100):
        if start:
            break
        for j in range(100):
            if board[i][j] == '2':
                start = (i, j)
                break

    print(f'#{t} {bfs(start)}')
