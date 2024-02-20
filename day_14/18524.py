import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections


def count_child(node: int) -> int:
    child = 1
    for idx in range(len(graph[node])):
        child += count_child(graph[node][idx])
    return child


T = int(input())

for t in range(1, T + 1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    graph = collections.defaultdict(list)
    for i in range(0, 2 * E, 2):
        graph[edges[i]].append(edges[i + 1])

    print(f'#{t} {count_child(N)}')
