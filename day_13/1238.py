import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections


def bfs() -> int:
    que = collections.deque([src])
    visited = [0] * 101
    visited[src] += 1

    sub_lst = []
    level = 0
    while que:
        vertex = que.popleft()
        for v in graph[vertex]:
            if not visited[v]:
                que.append(v)
                visited[v] = visited[vertex] + 1

                if visited[v] == level:
                    sub_lst.append(v)
                else:
                    sub_lst = [v]
                    level += 1

    result = 0
    for num in sub_lst:
        if num > result:
            result = num
    return result


for t in range(1, 11):
    N, src = map(int, input().split())
    lst = list(map(int, input().split()))

    graph = [set() for _ in range(101)]
    for i in range(0, N, 2):
        graph[lst[i]].add(lst[i + 1])

    print(f'#{t} {bfs()}')
