import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())

    primes = [2, 3, 5, 7, 11]
    result = [0] * 5
    for i, n in enumerate(primes):
        cnt = 0
        while not N % n:
            N //= n
            cnt += 1
        result[i] = str(cnt)
    print(f'#{t} {" ".join(result)}')
