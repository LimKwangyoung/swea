import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for row in range(N):
        for col in range(N):
            total = flies[row][col]
            ver_1 = ver_2 = 0
            for i in range(1, M):
                coord_1 = ((row - i, col), (row, col - i), (row, col + i), (row + i, col))
                coord_2 = ((row - i, col - i), (row - i, col + i), (row + i, col - i), (row + i, col + i))
                for r, c in coord_1:
                    if 0 <= r < N and 0 <= c < N:
                        ver_1 += flies[r][c]
                for r, c in coord_2:
                    if 0 <= r < N and 0 <= c < N:
                        ver_2 += flies[r][c]
            result = max(result, total + max(ver_1, ver_2))
    print(f'#{t} {result}')
