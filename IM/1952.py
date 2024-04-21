import sys

sys.stdin = open('input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    costs = list(map(int, input().split()))  # [1 day, 1 month, 3 months, 1 year]
    plans = list(map(int, input().split()))

    payments = [0] * 12
    payments[0] = min(costs[0] * plans[0], costs[1])
    payments[1] = payments[0] + min(costs[0] * plans[1], costs[1])

    for i in range(2, 12):
        payments[i] = min(payments[i - 1] + min(costs[0] * plans[i], costs[1]), payments[i - 3] + costs[2])
    print(f'#{t} {min(payments[-1], costs[3])}')
