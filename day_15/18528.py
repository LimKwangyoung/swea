import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def insert(idx: int) -> None:
    if tree[idx]:
        return tree[idx]

    left = insert(2 * idx) if 2 * idx <= N else 0
    right = insert(2 * idx + 1) if 2 * idx + 1 <= N else 0
    tree[idx] = left + right
    return tree[idx]


T = int(input())

for t in range(1, T + 1):
    N, M, L = map(int, input().split())

    tree = [None] * (N + 1)
    for _ in range(M):
        num, val = map(int, input().split())
        tree[num] = val
    insert(1)
    print(f'#{t} {tree[L]}')
