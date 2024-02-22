import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())

    bit = ''
    for _ in range(N):
        bit += input().strip()

    print(f'#{t}', end=' ')
    for i in range(0, N * 10, 7):
        result = 0
        for j in range(7):
            result += 2 ** (6 - j) * int(bit[i + j])
        print(result, end=' ')
