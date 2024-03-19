import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def dfs(level: int, total: int, path: set) -> None:
    global result

    if total > result:
        return

    if level == N:
        result = min(result, total)
        return

    for i in range(N):
        if i not in path:
            path.add(i)
            dfs(level + 1, total + products[level][i], path)
            path.remove(i)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    products = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')
    dfs(0, 0, set())
    print(f'#{tc} {result}')
