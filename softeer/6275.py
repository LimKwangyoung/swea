import sys


def find_start(row: int, col: int) -> tuple:
    visited = [[False] * W for _ in range(H)]
    stack = [(row, col)]
    while stack:
        row, col = stack.pop()
        visited[row][col] = True
        coord = ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col))
        cnt = 0
        for r, c in coord:
            if 0 <= r < H and 0 <= c < W and board[r][c] == '#' and not visited[r][c]:
                stack.append((r, c))
                cnt += 1
        if not cnt:
            return row, col


def moving(row: int, col: int, direction: int) -> None:
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

    stack = [(row, col, direction)]
    while stack:
        row, col, direction = stack.pop()
        board[row][col] = '.'

        for new_direction, (dr, dc) in enumerate(delta):
            r = row + dr
            c = col + dc
            if 0 <= r < H and 0 <= c < W and board[r][c] == '#':
                # straight
                if direction == new_direction:
                    print('A', end='')
                    board[r][c] = '.'
                    stack.append((r + dr, c + dc, new_direction))
                # turn
                else:
                    if (direction + 1) % 4 == new_direction:
                        print('R', end='')
                    else:
                        print('L', end='')
                    stack.append((row, col, new_direction))
                break


H, W = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(H)]

# find the start point
start = None
for i in range(H):
    if start:
        break
    for j in range(W):
        if board[i][j] == '#':
            start = find_start(i, j)

# initial position and direction
position = {0: '^', 1: '>', 2: 'v', 3: '<'}
init_coord = ((start[0] - 1, start[1]), (start[0], start[1] + 1), (start[0] + 1, start[1]), (start[0], start[1] - 1))
for idx, (i, j) in enumerate(init_coord):
    if 0 <= i < H and 0 <= j < W and board[i][j] == '#':
        pos = position[idx]
        break
print(start[0] + 1, start[1] + 1)
print(pos)

# path
moving(start[0], start[1], idx)
