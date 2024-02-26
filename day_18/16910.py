import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())

    result = 4 * N + 1
    part = 0
    for i in range(1, N + 1):
        part += int((N ** 2 - i ** 2) ** (1 / 2))
    print(f'#{t} {result + 4 * part}')
