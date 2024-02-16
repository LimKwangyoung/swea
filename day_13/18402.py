import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections


def bfs(src: int, dst: int) -> int:
    que = collections.deque([(src, 0)])  # (node, number of edges)
    visited = [False] * (V + 1)
    visited[src] = True
    while que:
        vertex, cnt = que.popleft()
        for v in graph[vertex]:
            if v == dst:
                return cnt + 1
            if not visited[v]:
                que.append((v, cnt + 1))
                visited[v] = True
    return 0


T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)
    S, G = map(int, input().split())

    print(f'#{t} {bfs(S, G)}')
