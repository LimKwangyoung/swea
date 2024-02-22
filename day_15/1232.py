import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def calculate(node: int) -> float:
    if values[node] not in '+-*/':
        return float(values[node])

    left = calculate(tree[node][0])
    right = calculate(tree[node][1])
    if values[node] == '+':
        values[node] = left + right
    elif values[node] == '-':
        values[node] = left - right
    elif values[node] == '*':
        values[node] = left * right
    else:
        values[node] = left / right
    return values[node]


for t in range(1, 11):
    N = int(input())

    tree = dict()
    values = [None] * (N + 1)
    for _ in range(N):
        num, value, *child = input().split()
        tree[int(num)] = list(map(int, child))
        values[int(num)] = value
    calculate(1)
    print(f'#{t} {int(values[1])}')
