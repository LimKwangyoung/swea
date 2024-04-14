import sys

sys.stdin = open('input.txt')
##################################################
IN = {
    0: (1, 2, 5, 6),
    1: (1, 3, 6, 7),
    2: (1, 2, 4, 7),
    3: (1, 3, 4, 5),
}

OUT = {
    1: (0, 1, 2, 3),
    2: (0, 2),
    3: (1, 3),
    4: (0, 1),
    5: (1, 2),
    6: (2, 3),
    7: (0, 3),
}

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

T = int(input())

for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 1
    que = [(R, C, board[R][C])]  # (row, col, status)
    board[R][C] = 0
    while que and L > 1:
        new_que = []
        for row, col, status in que:
            for i in OUT[status]:
                r = row + delta[i][0]
                c = col + delta[i][1]

                if 0 <= r < N and 0 <= c < M and board[r][c]:
                    num = board[r][c]
                    if num in IN[i]:
                        new_que.append((r, c, num))
                        board[r][c] = 0
                        result += 1
        que = new_que
        L -= 1
    print(f'#{t} {result}')
