import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def omok(row: int, col: int, cnt: list) -> None:
    global ans
    if board[row][col] == '.' or ans:
        return
    for num in cnt:
        if num >= 5:
            ans = True
            return

    # visited[row][col] = True
    # vertical
    if 0 <= row + 1 <= N - (5 - cnt[0]) and board[row + 1][col] == 'o':
        cnt[0] += 1
        omok(row + 1, col, cnt)
        cnt[0] = 1
    # horizon
    if 0 <= col + 1 <= N - (5 - cnt[1]) and board[row][col + 1] == 'o':
        cnt[1] += 1
        omok(row, col + 1, cnt)
        cnt[1] = 1
    # diagonal
    if 0 <= row + 1 <= N - (5 - cnt[2]) and 0 <= col + 1 <= N - (5 - cnt[2]) and board[row + 1][col + 1] == 'o':
        cnt[2] += 1
        omok(row + 1, col + 1, cnt)
        cnt[2] = 1
    # reverse diagonal
    if 0 <= row + 1 <= N - (5 - cnt[3]) and col >= 5 - cnt[3] and board[row + 1][col - 1] == 'o':
        cnt[3] += 1
        omok(row + 1, col - 1, cnt)
        cnt[3] = 1


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    ans = False
    for i in range(N):
        if ans:
            break
        for j in range(N):
            if board[i][j] == 'o':
                visited = [[False] * N for _ in range(N)]
                omok(i, j, [1, 1, 1, 1])
                if ans:
                    break
    print(f'#{t} {"YES" if ans else "NO"}')
