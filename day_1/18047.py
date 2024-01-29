import sys

sys.stdin = open('18047_input.txt')
##################################################


def cal_max(arr: list) -> int:
    maximum = arr[0]
    for num in arr[1:]:
        if maximum < num:
            maximum = num
    return maximum


def cal_min(arr: list) -> int:
    minimum = arr[0]
    for num in arr[1:]:
        if num < minimum:
            minimum = num
    return minimum


def cal_sum(arr: list) -> int:
    total = 0
    for num in arr:
        total += num
    return total


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    lst = []
    for i in range(N - M + 1):
        lst.append(cal_sum(nums[i:i + M]))
    print(f'#{t} {cal_max(lst) - cal_min(lst)}')
