import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def ternary_search(num: int):
    if num == 1:
        return 1
    left, right = 1, num
    while left < right:
        pl, pr = (2 * left + right) // 3, (left + 2 * right) // 3
        if pl == pr:
            break
        if pl ** 3 == num:
            return pl
        if pr ** 3 == num:
            return pr
        if pl ** 3 > num:
            right = pl
        elif pr ** 3 > num:
            left, right = pl, pr
        else:
            left = pr
    return -1


T = int(input())

for t in range(1, T + 1):
    print(f'#{t} {ternary_search(int(input()))}')
