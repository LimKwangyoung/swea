import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    string = ''
    for i in input():
        string += str(bin(int(i, 16)))[2:].zfill(4)

    print(f'#{t}', end=' ')
    for i in range(0, len(string), 7):
        bit = string[i:i + 7].zfill(8)
        print(int(bit, 2), end=' ')
    print()
