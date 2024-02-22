import sys

sys.stdin = open(f'input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    nums = input()

    result = set()
    for start in range(N // 4):
        for i in range(0, N, N // 4):
            num = ''
            for j in range(N // 4):
                num += nums[(start + i + j) % N]
            result.add(int(num, 16))
    print(f'#{t} {sorted(result, reverse=True)[K - 1]}')
