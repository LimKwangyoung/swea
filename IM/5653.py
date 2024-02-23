import sys

sys.stdin = open(f'input.txt')
##################################################
import collections


def bfs() -> int:
    global K

    cnt = K
    que = collections.deque(coord_lst)
    while cnt:
        new_queue = collections.deque()
        while que:
            row, col = que.popleft()
            # deactivate
            if board[row][col][0] > 0:
                board[row][col][0] -= 1
                new_queue.append((row, col))
            # activate
            elif board[row][col][1] > 0:
                board[row][col][1] -= 1
                if board[row][col][1] >= 1:
                    new_queue.append((row, col))
                # breeding
                coord = ((row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1))
                for r, c in coord:
                    if 0 <= r < N + 2 * K and 0 <= c < M + 2 * K and board[r][c][2] in (0, cnt - 1):
                        maximum = max(board[r][c][1], board[row][col][1] + 1)
                        board[r][c][0] = maximum
                        board[r][c][1] = maximum
                        board[r][c][2] = cnt - 1

                        if (r, c) not in set(new_queue):
                            new_queue.append((r, c))
        que = new_queue
        cnt -= 1
    return len(que)


T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    cells = [list(map(int, input().split())) for _ in range(N)]

    board = [[None] * (M + 2 * K) for _ in range(N + 2 * K)]
    for i in range(N + 2 * K):
        for j in range(M + 2 * K):
            board[i][j] = [0, 0, 0]
    coord_lst = []
    for i in range(N):
        for j in range(M):
            if cells[i][j]:
                board[i + K][j + K] = [cells[i][j], cells[i][j], K]  # [deactivate, activate, level]
                coord_lst.append([i + K, j + K])
    print(f'#{t} {bfs()}')
