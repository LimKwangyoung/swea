import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def square_root(num: int) -> int:
    i = 1
    while i * i <= num:
        i += 1
    return i - 1


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    part = 0
    for x in range(1, N):
        part += square_root(N**2 - x**2)
    result = 1 + 4 * (N + part)
    print(f'#{t} {result}')
