import sys

sys.stdin = open('input.txt')
##################################################


# Solution 1
def service(row: int, col: int, radius: int):
    operating_cost = radius ** 2 + (radius - 1) ** 2
    houses = 0
    for r in range(radius):
        for c in range(col - r, col + r + 1):
            if 0 <= row - radius + r + 1 < N and 0 <= c < N and board[row - radius + r + 1][c] == '1':
                houses += 1
    for r in range(1, radius):
        for c in range(col - (radius - 1 - r), col + (radius - 1 - r) + 1):
            if 0 <= row + r < N and 0 <= c < N and board[row + r][c] == '1':
                houses += 1
    if houses * M - operating_cost >= 0:
        return houses
    return False


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input().split() for _ in range(N)]

    # calculate range
    K = N
    if not N % 2:
        K += 1

    result = 0
    for i in range(N):
        for j in range(N):
            for k in range(K, 0, -1):
                ans = service(i, j, k)
                if ans:
                    result = max(result, ans)
    print(f'#{t} {result}')

# Solution 2
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    houses = []
    for i in range(N):
        for j, val in enumerate(input().split()):
            if val == '1':
                houses.append((i, j))

    result = 0
    for row in range(N):
        for col in range(N):
            distances = [abs(row - i) + abs(col - j) + 1 for i, j in houses]

            counts = [0] * (2 * N)
            for dist in distances:
                counts[dist] += 1
            for i in range(2, 2 * N):
                counts[i] += counts[i - 1]

            for k in range(2 * N - 1, 0, -1):
                if counts[k] * M >= k ** 2 + (k - 1) ** 2 and counts[k] > result:
                    result = counts[k]
    print(f'#{t} {result}')
