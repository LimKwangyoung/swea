import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import itertools
import heapq


def find(node: int) -> int:
    while node != parents[node]:
        node = parents[node]
    return node


def union(node_1: int, node_2: int) -> bool:
    root_1 = find(node_1)
    root_2 = find(node_2)
    if root_1 == root_2:
        return False

    if ranks[root_2] < ranks[root_1]:
        parents[root_2] = root_1
    else:
        if ranks[root_2] == ranks[root_1]:
            ranks[root_2] += 1
        parents[root_1] = root_2
    return True


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    distances = []
    for i, j in itertools.combinations(range(N), 2):
        heapq.heappush(distances, (E * ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2), i, j))

    result = 0
    cnt = 0
    parents = [i for i in range(N)]
    ranks = [0 for i in range(N)]
    while distances:
        dist, vertex_1, vertex_2 = heapq.heappop(distances)
        ans = union(vertex_1, vertex_2)
        if ans:
            result += dist
            cnt += 1
        else:
            continue

        if cnt == N - 1:
            break
    print(f'#{t} {round(result)}')
