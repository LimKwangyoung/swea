import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def dfs(row: int, col: int, level: int, path: str) -> None:
    if level == 7:
        if path not in used:
            used.add(path)
        return

    coord = [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]
    for r, c in coord:
        if 0 <= r < 4 and 0 <= c < 4:
            dfs(r, c, level + 1, path + board[r][c])


T = int(input())

for t in range(1, T + 1):
    board = [input().split() for _ in range(4)]

    used = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, board[i][j])
    print(f'#{t} {len(used)}')
