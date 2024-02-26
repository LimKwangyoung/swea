import sys

sys.stdin = open('input.txt')
##################################################


def runway(fix: int) -> int:
    def check(arr: list) -> int:
        prev = 0
        prev_height, prev_cnt = arr[prev]
        for cur in range(1, len(arr)):
            cur_height, cur_cnt = arr[cur]
            if prev_height < cur_height:
                if prev_cnt < X:
                    return 0
                else:
                    arr[prev][1] -= X
            if prev_height > cur_height:
                if cur_cnt < X:
                    return 0
                else:
                    arr[cur][1] -= X
            prev = cur
            prev_height, prev_cnt = arr[prev]
        return 1

    # horizon
    heights_1 = []
    idx = 0
    while idx < N:
        cnt = 1
        while idx < N - 1 and board[fix][idx] == board[fix][idx + 1]:
            cnt += 1
            idx += 1
        heights_1.append([board[fix][idx], cnt])  # [height, count]
        idx += 1

    # vertical
    heights_2 = []
    idx = 0
    while idx < N:
        cnt = 1
        while idx < N - 1 and board[idx][fix] == board[idx + 1][fix]:
            cnt += 1
            idx += 1
        heights_2.append([board[idx][fix], cnt])  # [height, count]
        idx += 1
    return check(heights_1) + check(heights_2)


T = int(input())

for t in range(1, T + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        result += runway(i)
    print(f'#{t} {result}')