import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    codes = input().split()

    stack = []
    for code in codes:
        if code not in '+-*/.':
            stack.append(int(code))
        elif code == '.':
            if len(stack) != 1:
                print(f'#{t} error')
            else:
                print(f'#{t} {stack.pop()}')
            break
        else:
            if len(stack) <= 1:
                print(f'#{t} error')
                break
            else:
                x2, x1 = stack.pop(), stack.pop()
                if code == '+':
                    stack.append(x1 + x2)
                elif code == '-':
                    stack.append(x1 - x2)
                elif code == '*':
                    stack.append(x1 * x2)
                else:
                    stack.append(x1 // x2)
