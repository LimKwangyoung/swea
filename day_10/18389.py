import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    incoming = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
    instack = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

    print(f'#{t} ', end='')
    stack = []
    for token in input():
        if token not in '+-*/()':
            print(token, end='')
        elif token == ')':
            while stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()
        elif token == '(' or not stack or incoming[token] > instack[stack[-1]]:
            stack.append(token)
        else:
            while incoming[token] < instack[stack[-1]]:
                print(stack.pop(), end='')
            stack.append(token)
    while stack:
        print(stack.pop(), end='')
