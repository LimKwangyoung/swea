import sys

sys.stdin = open('18046_input.txt')
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


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    print(f'#{t} {cal_max(nums) - cal_min(nums)}')
