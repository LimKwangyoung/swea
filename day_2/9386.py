import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
# Solution 1
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    seq = input()

    idx = 0
    result = 0
    while idx < N:
        cnt = 0
        while idx < N - 1 and seq[idx] == seq[idx + 1] == '1':
            idx += 1
            cnt += 1

        idx += 1
        cnt += 1
        if result < cnt:
            result = cnt
    print(f'#{t} {result}')

# Solution 2
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    seq = input()

    cnt = 0
    result = 0
    for n in seq:
        if n == '0':
            if result < cnt:
                result = cnt
            cnt = 0
        else:
            cnt += 1
    if result < cnt:
        result = cnt
    print(f'#{t} {result}')
