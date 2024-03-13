import sys

N, M = map(int, sys.stdin.readline().split())
restricted = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
test = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

idx_1 = idx_2 = 0
height_1 = restricted[idx_1][0]
height_2 = test[idx_2][0]
result = 0
while height_1 < 100 and height_2 < 100:
    result = max(result, test[idx_2][1] - restricted[idx_1][1])
    if height_1 < height_2:
        idx_1 += 1
        height_1 += restricted[idx_1][0]
    elif height_1 > height_2:
        idx_2 += 1
        height_2 += test[idx_2][0]
    else:
        idx_1 += 1
        idx_2 += 1
        height_1 += restricted[idx_1][0]
        height_2 += test[idx_2][0]

if height_1 == height_2 == 100:
    result = max(result, test[idx_2][1] - restricted[idx_1][1])
elif idx_1 < N - 1:
    while idx_1 < N:
        result = max(result, test[idx_2][1] - restricted[idx_1][1])
        idx_1 += 1
else:
    while idx_2 < M:
        result = max(result, test[idx_2][1] - restricted[idx_1][1])
        idx_2 += 1
print(result)