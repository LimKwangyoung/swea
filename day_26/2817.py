import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def dfs(idx: int, total: int) -> None:
    global result

    if total >= K:
        if total == K:
            result += 1
        return

    for i in range(idx, N):
        dfs(i + 1, total + nums[i])


T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    result = 0
    dfs(0, 0)
    print(f'#{t} {result}')