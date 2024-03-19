import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections


def preorder(node: str) -> None:
    print(node, end=' ')
    for v in graph[node]:
        preorder(v)


V = int(input())
vertex = input().split()

graph = collections.defaultdict(list)
for i in range(0, len(vertex), 2):
    graph[vertex[i]].append(vertex[i + 1])
preorder('1')
