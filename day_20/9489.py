import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input().split() for _ in range(N)]

    result = 0
    for i in range(N):
        result = max(result, len(max(''.join(board[i]).split('0'), key=len)))
    for i in range(M):
        result = max(result, len(max(''.join([board[j][i] for j in range(N)]).split('0'), key=len)))
    print(f'#{t} {result}')
