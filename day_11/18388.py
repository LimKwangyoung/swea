import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def dfs(row: int, total: int, level: int, visited: int) -> None:
    global result
    if total >= result:
        return
    if level == N and total < result:
        result = total
        return

    for i in range(N):
        if not visited & (1 << i):
            dfs(row + 1, total + board[row][i], level + 1, visited | (1 << i))


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')
    dfs(row=0, total=0, level=0, visited=0)
    print(f'#{t} {result}')
