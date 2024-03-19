import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def success(level: int, total: float, path: set) -> None:
    global result

    if total <= result:
        return

    if level == N:
        result = max(result, total)
        return

    for i in range(N):
        if i not in path and prob[level][i]:
            path.add(i)
            success(level + 1, total * prob[level][i], path)
            path.remove(i)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    prob = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]

    result = float('-inf')
    success(0, 1, set())
    print(f'#{t} {result * 100:.6f}')
