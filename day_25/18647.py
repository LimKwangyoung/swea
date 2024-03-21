import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections
import heapq


def dijkstra() -> list:
    distances = [float('inf')] * (N + 1)
    distances[0] = 0

    que = [(0, 0)]  # [distance, vertex]
    while que:
        dist, vertex = heapq.heappop(que)

        if distances[vertex] < dist:
            continue

        for info in graph[vertex]:
            new_dist = distances[vertex] + info[1]
            if new_dist < distances[info[0]]:
                distances[info[0]] = new_dist
                heapq.heappush(que, (new_dist, info[0]))
    return distances


T = int(input())

for t in range(1, T + 1):
    N, E = map(int, input().split())

    graph = collections.defaultdict(list)
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])  # [destination, distance]

    print(f'#{t} {dijkstra()[-1]}')
