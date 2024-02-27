import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def dfs(row: int, col: int) -> int:
    result = 1
    stack = [(row, col)]
    while stack:
        row, col = stack.pop()
        coord = ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col))
        for r, c in coord:
            if 0 <= r < N and 0 <= c < N and board[row][col] + 1 == board[r][c]:
                stack.append((r, c))
                result += 1
    return result


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]
    max_idx = []
    maximum = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                total = dfs(i, j)
                if total > maximum:
                    maximum = total
                    max_idx = [board[i][j]]
                elif total == maximum:
                    max_idx.append(board[i][j])
    print(f'#{t} {sorted(max_idx)[0]} {maximum}')
