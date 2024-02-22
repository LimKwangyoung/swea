import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]

    result = 'NO'
    for i in range(N):
        # horizon
        if 'ooooo' in board[i]:
            result = 'YES'
            break

        # vertical
        string = ''
        for j in range(N):
            string += board[j][i]
        if 'ooooo' in string:
            result = 'YES'
            break

    # diagonal
    for i in range(N - 4):
        string_1 = ''
        string_2 = ''
        for j in range(N - i):
            string_1 += board[j][i + j]
            string_2 += board[N - 1 - j][i + j]
        if 'ooooo' in string_1 or 'ooooo' in string_2:
            result = 'YES'
            break
    for i in range(1, N - 4):
        string_1 = ''
        string_2 = ''
        for j in range(N - i):
            string_1 += board[i + j][j]
            string_2 += board[N - 1 - i - j][j]
        if 'ooooo' in string_1 or 'ooooo' in string_2:
            result = 'YES'
            break

    print(f'#{t} {result}')
