import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    costs = list(map(int, input().split()))

    result = maximum = 0
    for i in range(N - 1, -1, -1):
        if costs[i] > maximum:
            maximum = costs[i]
        else:
            result += maximum - costs[i]
    print(f'#{t} {result}')
