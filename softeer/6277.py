import sys


def boxing(idx: int, min_x: int, min_y: int, max_x: int, max_y: int) -> None:
    global result

    area = (max_x - min_x) * (max_y - min_y)
    if area >= result:
        return

    if idx == K + 1:
        result = area
        return

    for x, y in colors[idx]:
        boxing(idx + 1, min(min_x, x), min(min_y, y), max(max_x, x), max(max_y, y))


N, K = map(int, sys.stdin.readline().split())

colors = [[] for _ in range(K + 1)]
for _ in range(N):
    *coord, color = map(int, sys.stdin.readline().split())
    colors[color].append(coord)

result = float('inf')
boxing(1, 1000, 1000, -1000, -1000)
print(result)
