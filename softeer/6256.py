import sys
import collections

numbering = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

N = int(sys.stdin.readline())

intersections = [collections.deque() for _ in range(4)]
for i in range(N):
    time, area = sys.stdin.readline().split()
    intersections[numbering[area]].append([int(time), i])  # [time, id of cars]

result = [-1] * N
time = -1
cnt = N
while N:
    minimum = min(car[0][0] for car in intersections if car)
    if minimum > time:
        time = minimum
    else:
        time += 1

    passes = []
    for i in range(4):
        if intersections[i] and intersections[i][0][0] <= time and (not intersections[(i - 1) % 4] or intersections[(i - 1) % 4][0][0] > time):
            passes.append(i)
    if not passes:
        break
    for i in passes:
        _, idx = intersections[i].popleft()
        result[idx] = time
        N -= 1

for i in result:
    print(i)
