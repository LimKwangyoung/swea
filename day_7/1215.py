import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
for t in range(1, 11):
    N = int(input())
    board = list(input() for _ in range(8))

    cnt = 0
    for i in range(8 - N + 1):
        for j in range(8 - N + 1):
            for n in range(N // 2):
                if board[i][j + n] != board[i][j + N - 1 - n]:
                    break
            else:
                cnt += 1
            for n in range(N // 2):
                if board[j + n][i] != board[j + N - 1 - n][i]:
                    break
            else:
                cnt += 1
    for i in range(8 - N + 1, 8):
        for j in range(8 - N + 1):
            for n in range(N // 2):
                if board[i][j + n] != board[i][j + N - 1 - n]:
                    break
            else:
                cnt += 1
            for n in range(N // 2):
                if board[j + n][i] != board[j + N - 1 - n][i]:
                    break
            else:
                cnt += 1
    print(f'#{t} {cnt}')
