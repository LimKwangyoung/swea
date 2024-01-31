import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
for _ in range(1, 11):
    t = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    result = float('-inf')
    diagonal = 0
    reverse_diagonal = 0
    for i in range(100):
        row_total = 0
        col_total = 0
        for j in range(100):
            row_total += board[i][j]
            col_total += board[j][i]

        diagonal += board[i][j]
        reverse_diagonal += board[i][99 - i]

        if result < row_total:
            result = row_total
        if result < col_total:
            result = col_total

    if result < diagonal:
        result = diagonal
    if result < reverse_diagonal:
        result = reverse_diagonal

    print(f'#{t} {result}')
