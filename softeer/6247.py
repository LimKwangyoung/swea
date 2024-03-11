import sys
import collections

# Solution 1
n, q = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
expectations = [int(input()) for _ in range(q)]

counts = collections.defaultdict(int)
counts[nums[0]] = 0
for i in range(1, n):
    counts[nums[i]] = counts[nums[i - 1]] + 1

for num in expectations:
    print(counts[num] * (n - 1 - counts[num]))

# Solution 2
n, q = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

for _ in range(q):
    num = int(input())

    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == num:
            print(mid * (n - mid - 1))
            break
        if nums[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    else:
        print(0)
