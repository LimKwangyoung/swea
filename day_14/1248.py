import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections


# # Solution 1
# def count_child(node: int) -> None:
#     global result
#     result += 1
#
#     for idx in child[node]:
#         count_child(idx)
#
#
# T = int(input())
#
# for t in range(1, T + 1):
#     V, E, vertex_1, vertex_2 = map(int, input().split())
#     edges = list(map(int, input().split()))
#
#     parent = list(range(V + 1))
#     child = collections.defaultdict(list)
#     for i in range(0, 2 * E, 2):
#         parent[edges[i + 1]] = edges[i]
#         child[edges[i]].append(edges[i + 1])
#
#     set_1, set_2 = set(), set()
#     while not set_1 & set_2:
#         set_1.add(vertex_1)
#         set_2.add(vertex_2)
#
#         vertex_1 = parent[vertex_1]
#         vertex_2 = parent[vertex_2]
#     sub_root = list(set_1 & set_2)[0]
#
#     result = 0
#     count_child(sub_root)
#     print(f'#{t} {sub_root} {result}')

# Solution 2
def find_level(node: int) -> int:
    result = 1
    while node != 1:
        node = parent[node]
        result += 1
    return result


def count_child(node: int) -> int:
    global cnt
    for idx in child[node]:
        count_child(idx)
        cnt += 1


T = int(input())

for t in range(1, T + 1):
    V, E, vertex_1, vertex_2 = map(int, input().split())
    edges = list(map(int, input().split()))

    parent = list(range(V + 1))
    child = collections.defaultdict(list)
    for i in range(0, 2 * E, 2):
        parent[edges[i + 1]] = edges[i]
        child[edges[i]].append(edges[i + 1])

    level_1 = find_level(vertex_1)
    level_2 = find_level(vertex_2)

    if level_1 < level_2:
        vertex_1, vertex_2 = vertex_2, vertex_1
        level_1, level_2 = level_2, level_1

    while level_1 != level_2:
        vertex_1 = parent[vertex_1]
        level_1 -= 1

    while vertex_1 != vertex_2:
        vertex_1 = parent[vertex_1]
        vertex_2 = parent[vertex_2]

    cnt = 1
    count_child(vertex_1)
    print(f'#{t} {vertex_1} {cnt}')
