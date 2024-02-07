import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    stack = []
    for i in input():
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                print(f'#{t} -1')
                break
            stack.pop()
    else:
        print(f'#{t} {-1 if stack else 1}')
