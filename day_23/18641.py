import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def charging(idx: int, cnt: int) -> None:
    global result

    if cnt >= result:
        return

    if idx >= N - 1:
        result = min(result, cnt)
        return

    for i in range(idx + 1, idx + batteries[idx] + 1):
        charging(i, cnt + 1)


T = int(input())

for t in range(1, T + 1):
    N, *batteries = list(map(int, input().split()))

    result = float('inf')
    charging(0, -1)
    print(f'#{t} {result}')
