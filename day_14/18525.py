import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def count_child(node: int) -> int:
    left = count_child(2 * node) if 2 * node <= N else 0
    right = count_child(2 * node + 1) if 2 * node + 1 <= N else 0

    cnt[node] = (left, right)
    return left + right + 1


def insert_node(node: int, value: int) -> None:
    tree[node] = value - cnt[node][1]

    if 2 * node <= N:
        insert_node(2 * node, tree[node] - 1)
    if 2 * node + 1 <= N:
        insert_node(2 * node + 1, value)


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    cnt = [None] * (N + 1)
    tree = [None] * (N + 1)
    count_child(1)
    insert_node(1, N)
    print(f'#{t} {tree[1]} {tree[N // 2]}')
