import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    A, B = input().split()
    lst = A.split(B)

    print(f'#{t} {len(lst) - 1 + len("".join(lst))}')
