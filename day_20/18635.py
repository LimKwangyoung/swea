import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    weights = sorted(list(map(int, input().split())), reverse=True)
    loads = sorted(list(map(int, input().split())), reverse=True)

    result = 0
    i = j = 0
    while i < N and j < M:
        if weights[i] <= loads[j]:
            result += weights[i]
            j += 1
        i += 1
    print(f'#{t} {result}')
