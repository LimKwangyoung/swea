import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def find(node: int) -> int:
    while node != parents[node]:
        node = parents[node]
    return node


def union(node_1: int, node_2: int) -> None:
    root_1 = find(node_1)
    root_2 = find(node_2)

    if root_1 == root_2:
        return
    parents[root_2] = root_1


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    parents = [i for i in range(N + 1)]
    for i in range(0, 2 * M, 2):
        student_1, student_2 = nums[i], nums[i + 1]
        union(student_1, student_2)
    for i in range(1, N + 1):
        parents[i] = find(i)

    print(f'#{t} {len(set(parents)) - 1}')
