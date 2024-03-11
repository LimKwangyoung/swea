import collections

# Solution 1
n, q = map(int, input().split())
nums = sorted(list(map(int ,input().split())))
expectations = [int(input()) for _ in range(q)]

counts = collections.defaultdict(int)
counts[nums[0]] = 0
for i in range(1, n):
    counts[nums[i]] = counts[nums[i - 1]] + 1

for num in expectations:
    print(counts[num] * (n - 1 - counts[num]))

# Solution 2
n, q = map(int, input().split())
nums = sorted(list(map(int ,input().split())))

for _ in range(q):
    num = int(input())

    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    if left < n and nums[left] == num:
        print(left * (n - left - 1))
    else:
        print(0)
