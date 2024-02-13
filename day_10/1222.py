import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
for t in range(1, 11):
    _, expression = input(), input()

    stack, postfix = [], []
    for token in expression:
        if token != '+':
            postfix.append(int(token))
        else:
            while stack:
                postfix.append(stack.pop())
            stack.append(token)
    postfix += stack  # since the operator is only '+'

    result = 0
    stack = []
    for token in postfix:
        if token != '+':
            stack.append(token)
        else:
            stack.append(stack.pop() + stack.pop())
    print(f'#{t} {stack[0]}')
