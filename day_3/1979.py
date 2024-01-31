import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    board = [input().split() for _ in range(N)]

    result = 0
    for i in range(N):
        # horizontal
        cnt = 0
        for j in range(N):
            if board[i][j] == '1':
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1
        cnt = 0

        # vertical
        cnt = 0
        for j in range(N):
            if board[j][i] == '1':
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1
        cnt = 0

    print(f'#{t} {result}')
