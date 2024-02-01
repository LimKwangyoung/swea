import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
for _ in range(10):
    t = int(input())
    board = [list(input().split()) for _ in range(100)]

    row, col = 98, board[-1].index('2')
    while row != 0:
        board[row][col] = '0'
        # check left
        if col - 1 >= 0 and board[row][col - 1] == '1':
            col -= 1
        # check right
        elif col + 1 < 100 and board[row][col + 1] == '1':
            col += 1
        # up
        else:
            row -= 1

    print(f'#{t} {col}')
