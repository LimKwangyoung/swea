import sys
import collections

N = int(sys.stdin.readline())
board = [list(sys.stdin.readline()) for _ in range(N)]

result = []
for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            cnt = 1
            que = collections.deque([(i, j)])
            board[i][j] = '0'
            while que:
                row, col = que.popleft()
                coord = [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]
                for r, c in coord:
                    if 0 <= r < N and 0 <= c < N and board[r][c] == '1':
                        que.append((r, c))
                        board[r][c] = '0'
                        cnt += 1
            result.append(cnt)
result.sort()
print(len(result))
for i in result:
    print(i)
