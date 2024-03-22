import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def find(node: int) -> int:
    while node != parents[node]:
        node = parents[node]
    return node


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    persons = [list(map(int, input().split())) for _ in range(M)]

    parents = [i for i in range(N + 1)]
    for vertex_1, vertex_2 in persons:
        root_1 = find(vertex_1)
        root_2 = find(vertex_2)
        if root_1 == root_2:
            continue

        parents[root_1] = root_2

    for i in range(N + 1):
        parents[i] = find(i)

    print(f'#{t} {len(set(parents)) - 1}')
