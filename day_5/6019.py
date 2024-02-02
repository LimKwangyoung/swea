import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
# Solution 1
T = int(input())

for t in range(1, T + 1):
    D, A, B, F = map(int, input().split())

    print(f'#{t} {F * (D / (A + B))}')

# Solution 2
T = int(input())

for t in range(1, T + 1):
    D, A, B, F = map(int, input().split())

    n = time = 1
    total = 0
    while time > 10e-8:
        if n % 2:
            time = (D - (A + B) * total) / (F + B)
        else:
            time = (D - (A + B) * total) / (F + A)
        total += time
    print(f'#{t} {F * total}')
