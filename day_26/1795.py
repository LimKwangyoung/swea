import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections
import heapq


def dijkstra(graph: dict, src: int) -> list:
    distances = [0] + [float('inf')] * N
    distances[src] = 0
    que = [(0, src)]  # (distance, vertex)

    while que:
        distance, src = heapq.heappop(que)

        if src not in graph or distances[src] < distance:
            continue

        for dst, dist in graph[src]:
            new_dist = distance + dist
            if new_dist < distances[dst]:
                distances[dst] = new_dist
                heapq.heappush(que, (new_dist, dst))
    return distances


T = int(input())

for t in range(1, T + 1):
    N, M, X = map(int, input().split())

    graph_1 = collections.defaultdict(list)
    graph_2 = collections.defaultdict(list)
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph_1[x].append((y, c))  # [vertex, distance]
        graph_2[y].append((x, c))  # [vertex, distance]

    arr_1 = dijkstra(graph_1, X)
    arr_2 = dijkstra(graph_2, X)

    result = float('-inf')
    for val in zip(arr_1, arr_2):
        result = max(result, sum(val))
    print(f'#{t} {result}')
