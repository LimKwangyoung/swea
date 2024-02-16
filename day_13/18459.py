import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections


def bfs(vertex: int) -> list:
    result = [str(vertex)]

    que = collections.deque([vertex])
    visited = [False, True] + [False] * (V - 1)
    while que:
        vertex = que.popleft()
        for v in graph[vertex]:
            if not visited[v]:
                que.append(v)
                visited[v] = True
                result.append(str(v))
    return result


V, E = map(int, input().split())
lst = list(map(int, input().split()))

graph = [[] for _ in range(V + 1)]
for i in range(0, 2 * E, 2):
    graph[lst[i]].append(lst[i + 1])
    graph[lst[i + 1]].append(lst[i])

print(f'#1 {" ".join(bfs(1))}')
