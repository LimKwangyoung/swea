import sys

sys.stdin = open('input.txt')
##################################################
import collections

tunnel = {
    1: (0, 1, 2, 3),
    2: (0, 2),
    3: (1, 3),
    4: (0, 1),
    5: (1, 2),
    6: (2, 3),
    7: (0, 3),
}

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

T = int(input())

for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 1
    que = collections.deque([(R, C, 1)])  # (row, col, status, time)
    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True
    while que:
        r, c, time = que.popleft()

        if time == L:
            continue

        for s, i in enumerate(tunnel[board[r][c]]):
            row = r + delta[i][0]
            col = c + delta[i][1]

            if 0 <= row < N and 0 <= col < M and board[row][col] and not visited[row][col]:
                if board[r][c] == 1 or board[r][c] in tunnel[board[row][col]]:
                    visited[row][col] = True
                    que.append((row, col, time + 1))
                    result += 1

        # for ii in range(N):
        #     for jj in range(M):
        #         print(1 if visited[ii][jj] else 0, end=' ')
        #     print()
        # print()
    print(f'#{t} {result}')