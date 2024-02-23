import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
pattern = {'001101': '0', '010011': '1', '111011': '2', '110001': '3', '100011': '4',
           '110111': '5', '001011': '6', '111101': '7', '011001': '8', '101111': '9'}


T = int(input())

for t in range(1, T + 1):
    string = input().strip()

    code = ''
    for i in string:
        code += str(bin(int(i, 16))[2:]).zfill(4)

    for idx in range(len(code) - 1, -1, -1):
        if code[idx] == '1':
            break
    code = code[idx // 6:idx + 1]

    print(f'#{t}', end=' ')
    for i in range(0, len(code), 6):
        print(pattern[code[i:i + 6]], end=' ')
    print()
