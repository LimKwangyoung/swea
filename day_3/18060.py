import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
# Solution 1
T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())

    result = 0
    for i in range(1 << 12):
        cnt = 0
        total = 0
        for j in range(12):
            if i & (1 << j):
                cnt += 1
                total += j + 1
        if cnt == N and total == K:
            result += 1
    print(f'#{t} {result}')


# Solution 2
def subset(idx: int, order: int, num: int):
    if order > N or num > K:
        return
    if order == N and num == K:
        global result
        result += 1
        return

    for i in range(idx, 13):
        subset(i + 1, order + 1, num + i)


T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())

    result = 0
    subset(1, 0, 0)
    print(f'#{t} {result}')
