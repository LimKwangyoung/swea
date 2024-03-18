import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def dfs(total: int, idx: int) -> None:
    global result

    if result == 0 or total - B > result:
        return
    if total >= B:
        result = total - B
        return

    for i in range(idx + 1, N):
        dfs(total + heights[i], i)


T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    result = float('inf')
    dfs(total=0, idx=-1)
    print(f'#{t} {result}')
