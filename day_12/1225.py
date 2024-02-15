import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections

for t in range(1, 11):
    _, code = input(), collections.deque(map(int, input().split()))

    idx = 1
    while code[-1]:
        num = code.popleft() - 1 * idx
        if num < 0:
            num = 0
        code.append(num)

        idx = (idx + 1) % 6
        if idx == 0:
            idx += 1
    print(f'#{t} {" ".join(map(str, code))}')
