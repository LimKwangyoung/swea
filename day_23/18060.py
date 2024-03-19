import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def dfs(idx: int, level: int, total: int) -> None:
    global result

    if level >= N or total >= K:
        if level == N and total == K:
            result += 1
        return

    for i in range(idx, 13):
        dfs(i + 1, level + 1, total + i)


T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())

    result = 0
    dfs(1, 0, 0)
    print(f'#{t} {result}')
