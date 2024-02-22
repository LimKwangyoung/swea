import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def decoding(num: int) -> str:
    result = ''
    cnt = 1
    for idx in range(6):
        if code[num + idx] == code[num + idx + 1]:
            cnt += 1
        else:
            result += str(cnt)
            cnt = 1
    return code_dict[result + str(cnt)]


def is_valid(string: str) -> int:
    odd = 0
    for idx in range(0, 8, 2):
        odd += int(string[idx])
    even = 0
    for idx in range(1, 8, 2):
        even += int(string[idx])

    return odd + even if not (odd * 3 + even) % 10 else 0


code_dict = {'3211': '0', '2221': '1', '2122': '2', '1411': '3', '1132': '4',
             '1231': '5', '1114': '6', '1312': '7', '1213': '8', '3112': '9'}

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    codes = [input() for _ in range(N)]

    code = ''
    for i in range(N):
        if code:
            break
        for j in range(M - 1, -1, -1):
            if codes[i][j] == '1':
                code = codes[i][j - 55:j + 1]
                break
    decode = ''
    for i in range(0, 56, 7):
        decode += decoding(i)
    print(f'#{t} {is_valid(decode)}')
