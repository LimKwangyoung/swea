import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections

V, E = map(int, input().split())
nums = list(map(int, input().split()))

graph = collections.defaultdict(list)
for i in range(0, 2 * E, 2):
    graph[nums[i]].append(nums[i + 1])
    graph[nums[i + 1]].append(nums[i])

visited = [False] * (V + 1)
visited[1] = True
print('#1 1', end=' ')
que = collections.deque([1])
while que:
    vertex = que.popleft()
    for v in graph[vertex]:
        if not visited[v]:
            que.append(v)
            visited[v] = True
            print(v, end=' ')
