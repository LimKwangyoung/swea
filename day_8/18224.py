import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

brackets = {')': '(', '}': '{', ']': '['}
for t in range(1, T + 1):
    stack = []
    for i in input():
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack or brackets[i] != stack.pop():
                print(f'#{t} 0')
                break
    else:
        print(f'#{t} {0 if stack else 1}')
