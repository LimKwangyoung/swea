def dfs(position: list, target_idx: int) -> None:
    global result

    if position in targets[target_idx:]:
        if position == targets[target_idx]:
            target_idx += 1
            if target_idx == m:
                result += 1
                return
        else:
            return

    row, col = position
    coord = [[row - 1, col], [row, col - 1], [row, col + 1], [row + 1, col]]
    board[row][col] = '1'
    for r, c in coord:
        if 0 <= r < n and 0 <= c < n and board[r][c] == '0':
            board[r][c] = '1'
            dfs([r, c], target_idx)
            board[r][c] = '0'


n, m = map(int, input().split())
board = [input().split() for _ in range(n)]
targets = [list(map(lambda x: x - 1, map(int, input().split()))) for _ in range(m)]

result = 0
dfs(position=targets[0], target_idx=1)
print(result)
