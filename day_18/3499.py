import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cards = input().split()

    left, right = cards[:(N + 1) // 2], cards[(N + 1) // 2:]
    pl = pr = 0
    print(f'#{t}', end=' ')
    while pl < len(left) and pr < len(right):
        print(f'{left[pl]} {right[pr]}', end=' ')
        pl += 1
        pr += 1
    if pl < len(left):
        print(f'{left[pl]}', end='')
    print()
