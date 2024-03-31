import sys

sys.stdin = open('input.txt')
##################################################


def cal_profit(c: int, condition: int, total: int) -> None:
    global profit

    if condition > C:
        return

    profit = max(profit, total)
    for idx in range(c, col + M):
        cal_profit(idx + 1, condition + board[row][idx], total + board[row][idx] ** 2)


T = int(input())

for t in range(1, T + 1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    honey = [[0] * (N - M + 1) for _ in range(N)]
    rows = []
    for row in range(N):
        maximum = float('-inf')
        for col in range(N - M + 1):
            profit = float('-inf')
            cal_profit(col, 0, 0)
            honey[row][col] = profit

            maximum = max(maximum, profit)
        rows.append(maximum)

    # another row
    rows.sort(reverse=True)
    result = rows[0] + rows[1]

    # same row
    if 2 * M <= N:
        for i in range(N):
            for j in range(N - 2 * M + 1):
                result = max(result, honey[i][j] + max(honey[i][k] for k in range(j + M, N - M + 1)))
    print(f'#{t} {result}')
