import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    cuts = input()

    result = idx = 0
    stack = []
    while idx < len(cuts):
        if cuts[idx] == '(':
            if cuts[idx + 1] == ')':
                result += len(stack)
                idx += 2
                continue
            stack.append(cuts[idx])
        else:
            stack.pop()
            result += 1
        idx += 1

    print(f'#{t} {result + len(stack)}')
