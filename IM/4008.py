import sys

sys.stdin = open('input.txt')
##################################################


def operate(total: int, num_idx: int) -> None:
    global maximum, minimum

    if not sum(operator):
        if total > maximum:
            maximum = total
        if total < minimum:
            minimum = total
        return

    for idx in range(4):
        if operator[idx] >= 1:
            operator[idx] -= 1
            if idx == 0:
                operate(total + operands[num_idx], num_idx + 1)
            elif idx == 1:
                operate(total - operands[num_idx], num_idx + 1)
            elif idx == 2:
                operate(total * operands[num_idx], num_idx + 1)
            else:
                operate(int(total / operands[num_idx]), num_idx + 1)
            operator[idx] += 1


operator_dict = {0: '+', 1: '-', 2: '*', 3: '/'}

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    operator = list(map(int, input().split()))
    operands = list(map(int, input().split()))

    minimum, maximum = float('inf'), float('-inf')
    operate(operands[0], 1)
    print(f'#{t} {maximum - minimum}')
