import sys


# Solution 1
def driving(row: int, col: int, direction: int, time: int) -> None:
    if time == T + 1:
        return

    result.add((row, col))

    status = traffic_light[row][col][time % 4]
    if check[direction] == status % 4:
        for sign in signs[status]:
            r = row + delta[sign][0]
            c = col + delta[sign][1]
            if 0 <= r < N and 0 <= c < N:
                driving(r, c, sign, time + 1)


delta = ((-1, 0), (0, -1), (0, 1), (1, 0))  # (up, left, right, down)
signs = (
    (0, 2, 3), (1, 0, 2), (0, 1, 3), (1, 3, 2),
    (0, 2), (1, 0), (1, 3), (3, 2),
    (2, 3), (0, 2), (0, 1), (1, 3)
)
check = {0: 1, 1: 2, 2: 0, 3: 3}  # {direction: status}

N, T = map(int, sys.stdin.readline().split())

traffic_light = [[None] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        traffic_light[i][j] = list(map(lambda x: x - 1, map(int, sys.stdin.readline().split())))

result = set()
driving(row=0, col=0, direction=0, time=0)
print(len(result))


# Solution 2
def driving(row: int, col: int, direction: int, time: int) -> None:
    if time == T + 1 or (direction, time % 4) in visited[row][col]:
        return

    result.add((row, col))
    visited[row][col].add((direction, time % 4))

    status = traffic_light[row][col][time % 4]
    if check[direction] == status % 4:
        for sign in signs[status]:
            r = row + delta[sign][0]
            c = col + delta[sign][1]
            if 0 <= r < N and 0 <= c < N:
                driving(r, c, sign, time + 1)


delta = ((-1, 0), (0, -1), (0, 1), (1, 0))  # (up, left, right, down)
signs = (
    (0, 2, 3), (1, 0, 2), (0, 1, 3), (1, 3, 2),
    (0, 2), (1, 0), (1, 3), (3, 2),
    (2, 3), (0, 2), (0, 1), (1, 3)
)
check = {0: 1, 1: 2, 2: 0, 3: 3}  # {direction: status}

N, T = map(int, sys.stdin.readline().split())

traffic_light = [[None] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        traffic_light[i][j] = list(map(lambda x: x - 1, map(int, sys.stdin.readline().split())))

result = set()
visited = [[set() for _ in range(N)] for _ in range(N)]
driving(row=0, col=0, direction=0, time=0)
print(len(result))
