import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def decoding(row: int, col: int):
    def check(string: str, n: int):
        ratio = ''
        p = 0
        while p < len(string) - 1:
            cnt = 1
            while p < len(string) - 1 and string[p] == string[p + 1]:
                p += 1
                cnt += 1
            p += 1
            ratio += str(cnt // n)
        if len(ratio) == 3:
            ratio += '1'
        if ratio in pattern:
            return pattern[ratio]
        else:
            return False

    length = 1
    while 56 * length <= col:
        idx = col
        result = []
        for _ in range(8):
            code = board[row][idx - 7 * length + 1:idx + 1]
            ans = check(code, length)
            if ans:
                result.append(ans)
                idx -= 7 * length
            else:
                length += 1
                break
        else:
            return result[::-1]
    return False


def is_valid(arr: list) -> int:
    odd = 0
    for idx in range(0, 8, 2):
        odd += int(arr[idx])
    even = 0
    for idx in range(1, 7, 2):
        even += int(arr[idx])

    return odd + even + int(arr[-1]) if not (3 * odd + even + int(arr[-1])) % 10 else 0


pattern = {'3211': '0', '2221': '1', '2122': '2', '1411': '3', '1132': '4',
           '1231': '5', '1114': '6', '1312': '7', '1213': '8', '3112': '9'}


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        line = list(input())
        for i in range(M):
            if line[i] != '0':
                line[i] = str(bin(int(line[i], 16)))[2:].zfill(4)
        board.append(''.join(line))

    decode = 0
    for i in range(N):
        if decode:
            break
        j = len(board[i]) - 1
        while j >= 0:
            if board[i][j] != '0':
                decode = decoding(i, j)
                if decode:
                    decode = is_valid(decode)
                    if decode:
                        print(f'#{t} {decode}')
                        break
            j -= 1
    else:
        print(f'#{t} 0')


    # for i in board:
    #     print(i)