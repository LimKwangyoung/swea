import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def deadlock(col: int) -> int:
    result = row = 0
    while row < 100:
        if table[row][col] == '1':
            while row < 100 and table[row][col] != '2':
                row += 1

            if row >= 100:
                return result
            result += 1
        row += 1
    return result


for t in range(1, 11):
    input()
    table = [input().split() for _ in range(100)]

    total = 0
    for i in range(100):
        total += deadlock(i)
    print(f'#{t} {total}')
