import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def inorder(node: int) -> None:
    if 2 * node <= N:
        inorder(2 * node)
    print(alphabets[node], end='')
    if 2 * node + 1 <= N:
        inorder(2 * node + 1)


for t in range(1, 11):
    N = int(input())

    alphabets = dict()
    for _ in range(N):
        num, alphabet, *_ = input().split()
        alphabets[int(num)] = alphabet

    print(f'#{t}', end=' ')
    inorder(1)
    print()
