import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())

    # initialize first horizontal part
    snail = [list(map(str, range(1, N + 1)))] + [[None] * N for _ in range(N - 1)]

    num = N + 1
    length = N - 1
    x, y = 0, N - 1
    idx = 0
    coord = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    while length > 0:
        # vertical and horizontal
        for _ in range(2):
            dx, dy = coord[idx % 4]
            for _ in range(length):
                x += dx
                y += dy
                snail[x][y] = str(num)
                num += 1
            idx += 1
        length -= 1

    print(f'#{t}')
    for i in snail:
        print(' '.join(i))
