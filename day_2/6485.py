import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())

    buses = [list(map(int, input().split())) for _ in range(N)]

    P = int(input())
    stations = [int(input()) for _ in range(P)]

    result = [0] * P
    for i, station in enumerate(stations):
        cnt = 0
        for a, b in buses:
            if a <= station <= b:
                cnt += 1
        result[i] = str(cnt)
    print(f'#{t} {" ".join(result)}')
