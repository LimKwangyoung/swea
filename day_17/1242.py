import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


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


def is_valid(arr: str) -> int:
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

    line_check = set()
    code_lines = []
    for _ in range(N):
        line = input().strip().rstrip('0')
        if line == '' or line in line_check:
            continue

        line_check.add(line)
        line = list(line)
        for i, char in enumerate(line):
            line[i] = str(bin(int(char, 16)))[2:].zfill(4)
        line = ''.join(line).rstrip('0')
        code_lines.append(line)

    result = 0
    code_check = set()
    for line in code_lines:
        col = len(line)
        length = 1
        while col >= 55:
            i = col

            decode_lst = []
            for _ in range(8):
                code = line[i - 7 * length:i]
                ans = check(code, length)
                if ans:
                    decode_lst.append(ans)
                    i -= 7 * length
                else:
                    length += 1
                    break
            else:
                decode = ''.join(decode_lst[::-1])
                if decode not in code_check:
                    code_check.add(decode)
                    result += is_valid(decode)
                line = line[:i].rstrip('0')
                col = len(line)
                length = 1
    print(f'#{t} {result}')
