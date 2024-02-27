import sys

sys.stdin = open('input.txt')
##################################################
from itertools import permutations

operator_dict = {0: '+', 1: '-', 2: '*', 3: '/'}

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    operators = []
    for i, val in enumerate(map(int, input().split())):
        operators.extend([operator_dict[i]] * val)
    operators = permutations(operators, N - 1)

    operands = list(map(int, input().split()))
    used = set()
    minimum, maximum = float('inf'), float('-inf')
    for operator in operators:
        if operator not in used:
            used.add(operator)
            total = operands[0]
            for i, num in enumerate(operands[1:]):
                if operator[i] == '+':
                    total += num
                elif operator[i] == '-':
                    total -= num
                elif operator[i] == '*':
                    total *= num
                else:
                    total = int(total / num)
            minimum = min(minimum, total)
            maximum = max(maximum, total)
    print(f'#{t} {maximum - minimum}')
