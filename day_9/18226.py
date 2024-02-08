import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input()) // 10

    dp = [0] * (N + 1)
    dp[0] = dp[1] = 1
    for i in range(2, N + 1):
        dp[i] = 2 * dp[i - 2] + dp[i - 1]
    print(f'#{t} {dp[N]}')
