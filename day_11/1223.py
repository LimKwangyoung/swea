import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
for t in range(1, 11):
    _, expression = input(), input()

    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack, postfix = [], []
    for token in expression:
        if token not in '+-*/':
            postfix.append(token)
        else:
            while stack and priority[token] <= priority[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(token)
    while stack:
        postfix.append(stack.pop())

    stack = []
    for token in postfix:
        if token not in '+-*/':
            stack.append(int(token))
        else:
            x2, x1 = stack.pop(), stack.pop()
            if token == '+':
                stack.append(x1 + x2)
            elif token == '-':
                stack.append(x1 - x2)
            elif token == '*':
                stack.append(x1 * x2)
            else:
                stack.append(x1 / x2)
    print(f'#{t} {stack.pop()}')
