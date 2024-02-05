import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
#################################################
T = int(input())

for t in range(1, T + 1):
    str1 = input()
    str2 = input()

    print(f'#{t} {1 if str1 in str2 else 0}')
