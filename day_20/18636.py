import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    trucks = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))

    cnt = 1
    time = trucks[0][1]
    for i in range(1, N):
        start, end = trucks[i]
        if start < time:
            continue
        time = end
        cnt += 1
    print(f'#{t} {cnt}')
