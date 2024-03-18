import sys
import collections


def cal_cost(cost: int) -> int:
        return sum(((cost - power) ** 2) * powers[power] for power in powers if cost > power)


def binary_search(left: int, right: int) -> int:
    while left <= right:
        mid = (left + right) // 2
        if cal_cost(mid) <= B:
            left = mid + 1
        else:
            right = mid - 1
    return right


N, B = map(int, sys.stdin.readline().split())

powers = collections.defaultdict(int)
for i in map(int, sys.stdin.readline().split()):
    powers[i] += 1

print(binary_search(1, 2 * 10 ** 9))
