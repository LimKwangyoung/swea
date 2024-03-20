import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections

for t in range(1, 11):
    N, start = map(int, input().split())
    nums = list(map(int, input().split()))

    graph = collections.defaultdict(list)
    for i in range(0, N, 2):
        graph[nums[i]].append(nums[i + 1])

    visited = [0] * 101
    visited[start] = 1
    que = collections.deque([start])
    while que:
        vertex = que.popleft()
        for v in graph[vertex]:
            if not visited[v]:
                visited[v] = visited[vertex] + 1
                que.append(v)
    maximum = float('-inf')
    max_idx = None
    for i, val in enumerate(visited):
        if val >= maximum:
            maximum = val
            max_idx = i
    print(f'#{t} {max_idx}')
