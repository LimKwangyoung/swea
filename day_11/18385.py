import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def rsp(x: int, y: int) -> int:
    if cards[x] == cards[y]:  # draw
        return x
    elif cards[x] == '1':
        if cards[y] == '2':
            return y
        else:
            return x
    elif cards[x] == '2':
        if cards[y] == '1':
            return x
        else:
            return y
    else:
        if cards[y] == '1':
            return y
        else:
            return x


def game(start: int, end: int) -> int:
    if start + 1 == end:
        return rsp(start, end)
    if start == end:
        return start

    mid = (start + end) // 2
    left = game(start, mid)
    right = game(mid + 1, end)

    return rsp(left, right)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cards = [None] + input().split()

    print(f'#{t} {game(1, N)}')
