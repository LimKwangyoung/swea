import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


# Solution 1
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

# Solution 2
import collections
import math


def subsum(idx: int, cnt: int, total: int):
    global result
    if total >= K:
        if total == K:
            result += cnt
        return

    for i in range(idx, len(nums)):
        num = nums[i]
        for j in range(1, counts[num] + 1):
            if total + num * j > K:
                break
            subsum(i + 1, cnt * (math.factorial(counts[num]) // (math.factorial(j) * math.factorial(counts[num] - j))), total + num * j)


T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    counts = collections.defaultdict(int)
    for n in nums:
        counts[n] += 1
    nums = list(counts.keys())

    result = 0
    subsum(0, 1, 0)
    print(f'#{t} {result}')
