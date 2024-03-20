import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def dfs(vertex: int) -> None:
    if not visited[vertex]:
        visited[vertex] = True
        result.append(str(vertex))
        for v in graph[vertex]:
            dfs(v)


V, E = map(int, input().split())
nums = list(map(int, input().split()))

graph = dict()
for i in range(0, 2 * E, 2):
    if nums[i] not in graph:
        graph[nums[i]] = []
    if nums[i + 1] not in graph:
        graph[nums[i + 1]] = []
    graph[nums[i]].append(nums[i + 1])
    graph[nums[i + 1]].append(nums[i])

result = []
visited = [False] * (V + 1)
dfs(1)
print(f'#1 {"-".join(result)}')
