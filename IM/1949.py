import sys

sys.stdin = open('input.txt')
##################################################


def dfs(row: int, col: int, total: int, used: bool) -> None:
    global result
    result = max(result, total)

    current_height = board[row][col]
    coord = ((row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1))
    for r, c in coord:
        if 0 <= r < N and 0 <= c < N and not visited[r][c]:
            next_height = board[r][c]
            if current_height > next_height:
                visited[r][c] = True
                dfs(r, c, total + 1, used)
                visited[r][c] = False
            elif not used and current_height > next_height - K:
                visited[r][c] = True
                board[r][c] = board[row][col] - 1
                dfs(r, c, total + 1, True)
                visited[r][c] = False
                board[r][c] = next_height


T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())

    highest = float('-inf')
    board, highest_pos = [], []
    for i in range(N):
        lst = list(map(int, input().split()))
        for j in range(N):
            if highest == lst[j]:
                highest_pos.append((i, j))
            elif highest < lst[j]:
                highest_pos = [(i, j)]
                highest = lst[j]
        board.append(lst)

    result = float('-inf')
    visited = [[False] * N for _ in range(N)]
    for i, j in highest_pos:
        visited[i][j] = True
        dfs(row=i, col=j, total=1, used=False)
        visited[i][j] = False
    print(f'#{t} {result}')
