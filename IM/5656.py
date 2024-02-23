import sys

sys.stdin = open(f'input.txt')
##################################################
import copy


def search(cnt: int) -> None:
    def is_shoot(col: int):
        for row in range(H):
            if bricks[row][col]:
                return row, col
        return None, None

    def bomb(row: int, col: int, num: int) -> None:
        bricks[row][col] = 0
        bomb_lst = []
        for length in range(1, num):
            coord = ((row - length, col), (row, col + length), (row + length, col), (row, col - length))
            for r, c in coord:
                if 0 <= r < H and 0 <= c < W and bricks[r][c] > 0:
                    bomb_lst.append((r, c, bricks[r][c]))
                    bricks[r][c] = 0

        for r, c, n in bomb_lst:
            bomb(r, c, n)

    def gravity() -> None:
        global bricks

        new_bricks = [[0] * W for _ in range(H)]
        for col in range(W):
            idx = -1
            for row in range(H - 1, -1, -1):
                if bricks[row][col] > 0:
                    new_bricks[idx][col] = bricks[row][col]
                    idx -= 1
        bricks = new_bricks

    global bricks

    if cnt == N:
        total = 0
        for i in range(H):
            for j in range(W):
                if bricks[i][j]:
                    total += 1
        result.append(total)
        return

    flag = False
    for i in range(W):
        ans = is_shoot(i)
        if ans[0] is not None:
            # sub = copy.deepcopy(bricks)
            sub = [copy.copy(brick) for brick in bricks]
            bomb(ans[0], ans[1], bricks[ans[0]][ans[1]])
            gravity()
            search(cnt + 1)
            bricks = sub
            flag = True
    if not flag:
        search(N)


T = int(input())

for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]

    result = []
    search(0)
    print(f'#{t} {min(result)}')
