import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = float(input())

    result = ''
    cnt = 0
    while N != 0:
        if cnt >= 13:
            result = 'overflow'
            break

        N *= 2
        num, N = divmod(N * 10, 10)
        N /= 10
        result += str(int(num))
        cnt += 1
    print(f'#{t} {result}')
