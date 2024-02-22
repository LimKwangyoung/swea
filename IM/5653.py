import sys

sys.stdin = open(f'input.txt')
##################################################
import collections


def bfs() -> int:
    global K

    # (row, col, deactivate, activate, level)
    que = collections.deque([(row, col, board[row][col][0], board[row][col][1], K - 1) for row, col in coord_lst])
    while K and que:
        row, col, deac, ac, level = que.popleft()
        # deactivate
        if deac > 0:
            deac -= 1
        else:
            # activate
            coord = ((row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1))
            for r, c in coord:
                if 0 <= r < N + 2 * K and 0 <= c < M + 2 * K and board[r][c][1] in (0, level):
                    board[r][c] = max(board[r][c], (board[row][col], level), key=lambda x: x[1])
                    que.append(r, c, )
            board[row][col][1] -= 1
        K -= 1
    return len(que)


T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    coord_lst = [(i + K, j + K) for i in range(N) for j in range(M) if board[i][j]]
    board = [[(0, 0)] * (M + 2 * K) for _ in range(K)] + \
            [[(0, 0)] * K + [(board[i][j], K) for j in range(M)] + [(0, 0)] * K for i in range(N)] + \
            [[(0, 0)] * (M + 2 * K) for _ in range(K)]
    # for i in board:
    #     for j in i:
    #         print(j, end='')
    #     print()
    print(f'#{t} {bfs()}')
