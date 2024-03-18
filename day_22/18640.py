import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def binary_search(target: int) -> True:
    left, right = 0, A - 1
    prev = None
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True
        if nums[mid] < target:
            if prev == 0:
                return False
            left = mid + 1
            prev = 0
        else:
            if prev == 1:
                return False
            right = mid - 1
            prev = 1
    return False


T = int(input())

for t in range(1, T + 1):
    A, B = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    targets = list(map(int, input().split()))

    result = 0
    for i in targets:
        if binary_search(i):
            result += 1
    print(f'#{t} {result}')
