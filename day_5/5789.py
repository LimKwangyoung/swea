import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N, Q = map(int, input().split())
    result = ['0'] * N
    for num in range(Q):
        left, right = map(int, input().split())
        for i in range(left - 1,  right):
            result[i] = str(num + 1)
    print(f'#{t} {" ".join(result)}')
