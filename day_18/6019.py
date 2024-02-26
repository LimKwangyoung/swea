import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    D, A, B, F = map(int, input().split())

    print(f'#{t} {(D / (A + B)) * F}')
