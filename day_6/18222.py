import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
#################################################
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    flag = False
    for r in range(N):
        if flag:
            break
        for c in range(N):
            # horizon
            if 0 <= c < N - M + 1:
                words = board[r][c:c + M]
                for i in range(M // 2):
                    if words[i] != words[M - 1 - i]:
                        break
                else:
                    print(f'#{t} {words}')
                    flag = True
                    break
            # vertical
            if 0 <= r < N - M + 1:
                words = [board[i][c] for i in range(r, r + M)]
                for i in range(M // 2):
                    if words[i] != words[M - 1 - i]:
                        break
                else:
                    print(f'#{t} {"".join(words)}')
                    flag = True
                    break
