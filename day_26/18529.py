import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N, string = input().split()

    result = ''
    for s in string:
        result += str(bin(int(s, 16))[2:]).zfill(4)
    print(f'#{t} {result}')
