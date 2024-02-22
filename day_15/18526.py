import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def insert(node: int, value: int) -> None:
    tree[node] = value
    while node // 2 >= 1:
        parent = node // 2
        if tree[parent] > tree[node]:
            tree[parent], tree[node] = tree[node], tree[parent]
            node = parent
        else:
            return


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    tree = [None] * (N + 1)
    for i, val in enumerate(nums):
        insert(i + 1, val)

    result = 0
    while N // 2 >= 1:
        N //= 2
        result += tree[N]
    print(f'#{t} {result}')
