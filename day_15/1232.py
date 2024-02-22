import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections

def calculate(node: int) -> float:
    if tree[node] not in '+-*/':
        return float(tree[node])
    try:
        left = calculate(2 * node)
        right = calculate(2 * node + 1)
    except:
        print(node)

    if tree[node] == '+':
        tree[node] = left + right
    elif tree[node] == '-':
        tree[node] = left - right
    elif tree[node] == '*':
        tree[node] = left * right
    else:
        tree[node] = left / right
    return tree[node]


for t in range(1, 11):
    N = int(input())

    tree = collections.defaultdict(list)
    for _ in range(N):
        num, val, *child = input().split()
        tree[] = val
    calculate(1)
    print(f'#{t} {int(tree[1])}')
