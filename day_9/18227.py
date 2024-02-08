import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections


def dfs(src: int, dst: int) -> int:
    stack = [src]
    visited = [False] * (V + 1)
    while stack:
        vertex = stack.pop()
        if vertex == dst:
            return 1

        if not visited[vertex]:
            visited[vertex] = True
            for v in graph[vertex]:
                if not visited[v]:
                    stack.append(v)
    return 0


T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())

    graph = collections.defaultdict(list)
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
    S, G = map(int, input().split())

    print(f'#{t} {dfs(S, G)}')
