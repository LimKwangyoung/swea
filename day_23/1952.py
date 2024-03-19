import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    costs = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    dp = [0] * 12
    dp[0] = min(plan[0] * costs[0], costs[1])
    dp[1] = dp[0] + min(plan[1] * costs[0], costs[1])
    dp[2] = min(dp[1] + min(plan[2] * costs[0], costs[1]), costs[2])

    for i in range(3, 12):
        dp[i] = min(dp[i - 1] + min(plan[i] * costs[0], costs[1]), dp[i - 3] + costs[2])
    print(f'#{t} {min(costs[3], dp[-1])}')
