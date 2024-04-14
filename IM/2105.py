import sys

sys.stdin = open('input.txt')
##################################################
import collections


def dfs(row: int, col: int, idx: int, nums: list, total: list) -> None:
    global result

    if idx == 3:
        if lines[row][col][3][total[1]]:
            candidates = lines[row][col][3][total[1]]
            if not set(nums) & set(candidates[:-1]) and nums[0] == candidates[-1]:
                result = max(result, 2 * sum(total))
        return

    if idx == 2:
        if lines[row][col][2][total[0]]:
            candidates = lines[row][col][2][total[0]]
            if not set(nums) & set(candidates):
                dfs(row + delta[idx][0] * total[0], col + delta[idx][1] * total[0], idx + 1, nums + candidates[:-1], total)
        return

    for length, candidates in lines[row][col][idx].items():
        if not set(nums) & set(candidates):
            dfs(row + delta[idx][0] * length, col + delta[idx][1] * length, idx + 1, nums + candidates[:-1], total + [length])


delta = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [input().split() for _ in range(N)]

    lines = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for di, dj in delta:
                i, j = r, c
                tmp = collections.defaultdict(list)

                lst = [board[i][j]]
                i += di
                j += dj

                cnt = 1
                while 0 <= i < N and 0 <= j < N:
                    if board[i][j] in lst:
                        break

                    lst.append(board[i][j])
                    tmp[cnt] = lst[:]

                    i += di
                    j += dj
                    cnt += 1
                lines[r][c].append(tmp)

    result = float('-inf')
    for r in range(N - 2):
        for c in range(1, N - 1):
            dfs(row=r, col=c, idx=0, nums=list(), total=list())
    print(f'#{t} {-1 if result == float("-inf") else result}')
