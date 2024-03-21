import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import heapq


def find(node: int) -> int:
    if node == parents[node]:
        return node
    parents[node] = find(parents[node])
    return parents[node]


def union(node_1: int, node_2: int) -> bool:
    root_1 = find(node_1)
    root_2 = find(node_2)

    if root_1 == root_2:
        return False
    parents[root_2] = root_1
    return True


T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())

    distances = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        heapq.heappush(distances, (w, n1, n2))

    result = 0
    cnt = 0
    parents = [i for i in range(V + 1)]
    while heapq:
        weight, vertex_1, vertex_2 = heapq.heappop(distances)
        ans = union(vertex_1, vertex_2)
        if ans:
            result += weight
            cnt += 1
        else:
            continue

        if cnt == V:
            break
    print(f'#{t} {result}')
