import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections

for _ in range(1, 11):
    t, N = map(int, input().split())
    edges = list(map(int, input().split()))

    graph = collections.defaultdict(list)
    for i in range(0, 2 * N, 2):
        graph[edges[i]].append(edges[i + 1])

    visited = [False] * 100
    stack = [0]
    while stack:
        vertex = stack.pop()
        if vertex == 99:
            print(f'#{t} 1')
            break

        if not visited[vertex]:
            visited[vertex] = True
            for i in graph[vertex]:
                if not visited[i]:
                    stack.append(i)
    else:
        print(f'#{t} 0')
