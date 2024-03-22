import sys


def cal_cost(lands: list) -> int:
    minimum = float('inf')
    for height in range(1, 4):
        minimum = min(minimum, sum(abs(height - land) for land in lands))
    return minimum


board = [list(map(int, input().split())) for _ in range(3)]

result = float('inf')
for i in range(3):
    result = min(result, cal_cost(board[i]))
    if not result:
        break

    result = min(result, cal_cost([board[j][i] for j in range(3)]))
    if not result:
        break
print(result)
