import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    new_board = [[None] * N for _ in range(N)]
    new_board[0][0] = board[0][0]
    que = collections.deque([(0, 0)])
    while que:
        row, col = que.popleft()
        for r, c in ((row, col + 1), (row + 1, col)):
            if 0 <= r < N and 0 <= c < N:
                if not new_board[r][c] or new_board[r][c] > new_board[row][col] + board[r][c]:
                    new_board[r][c] = new_board[row][col] + board[r][c]
                    que.append((r, c))
    print(f'#{t} {new_board[-1][-1]}')
