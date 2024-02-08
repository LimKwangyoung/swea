import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
V, E = map(int, input().split())
edges = list(map(int, input().split()))

graph = [[None] * (V + 1) for _ in range(V + 1)]
for i in range(0, 2 * E, 2):
    graph[edges[i]][edges[i + 1]] = True
    graph[edges[i + 1]][edges[i]] = True
visited = [None] * (V + 1)

result = []
stack = [1]
while stack:
    vertex = stack.pop()
    if not visited[vertex]:
        visited[vertex] = True
        result.append(str(vertex))

        for i in range(V, -1, -1):
            if graph[vertex][i] and not visited[i]:
                stack.append(i)

print(f'#1 {"-".join(result)}')
