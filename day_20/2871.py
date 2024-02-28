import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def subsum(idx: int, path: list):
    global result

    if sum(path) > K:
        return

    if sum(path) == K:
        result += 1
        return

    for i in range(idx + 1, N):
        subsum(i, path + [nums[i]])


T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    nums = sorted(list(map(int, input().split())))

    result = 0
    subsum(-1, [])
    print(f'#{t} {result}')
