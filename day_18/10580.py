import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N - 1):
        left, right = lines[i]
        for j in range(i + 1, N):
            l, r = lines[j]
            if (left - l) * (right - r) < 0:
                result += 1
    print(f'#{t} {result}')
