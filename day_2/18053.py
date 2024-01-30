import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    num = input()

    count = [0] * 10
    for i in num:
        count[int(i)] += 1

    idx, result = 9, count[-1]
    for i in range(8, -1, -1):
        if count[i] > result:
            idx = i
            result = count[i]
    print(f'#{t} {idx} {result}')
