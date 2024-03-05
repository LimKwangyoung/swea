def dfs(row: int, col: int, level: int):
    global flag

    if flag:
        return

    if (row, col) == end:
        flag = True
        return

    # up
    for idx in range(1, level + 1):
        if 0 <= row - idx < N and board[row - idx][col] != '0' and not visited[row - idx][col]:
            visited[row - idx][col] = True
            dfs(row - idx, col, level)
            break
    # down
    for idx in range(1, level + 1):
        if 0 <= row + idx < N and board[row + idx][col] != '0' and not visited[row + idx][col]:
            visited[row + idx][col] = True
            dfs(row + idx, col, level)
            break
    # left
    if 0 <= col - 1 < M and board[row][col - 1] != '0' and not visited[row][col - 1]:
        visited[row][col - 1] = True
        dfs(row, col - 1, level)

    # right
    if 0 <= col + 1 < M and board[row][col + 1] != '0' and not visited[row][col + 1]:
        visited[row][col + 1] = True
        dfs(row, col + 1, level)


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    board = []
    for i in range(N):
        lst = input().split()
        for j in range(M):
            if lst[j] == '2':
                start = (i, j)
            elif lst[j] == '3':
                end = (i, j)
        board.append(lst)

    result = 1
    flag = False
    while True:
        visited = [[False] * M for _ in range(N)]
        dfs(start[0], start[1], result)
        if flag:
            break
        result += 1
    print(f'#{t} {result}')
