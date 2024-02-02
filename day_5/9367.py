import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    result = cnt = 1
    for i in range(1, N):
        if carrots[i] == carrots[i - 1] + 1:
            cnt += 1
        else:
            if result < cnt:
                result = cnt
            cnt = 1
    if result < cnt:
        result = cnt
    print(f'#{t} {result}')
