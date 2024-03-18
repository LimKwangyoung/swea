import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def quick_sort(left: int, right: int) -> None:
    if left < right:
        mid = partition(left, right)
        quick_sort(left, mid - 1)
        quick_sort(mid + 1, right)


def partition(left: int, right: int) -> int:
    pivot = nums[left]
    pl, pr = left, right
    while pl <= pr:
        while pl <= pr and nums[pl] <= pivot:
            pl += 1
        while pl <= pr and nums[pr] >= pivot:
            pr -= 1
        if pl < pr:
            nums[pl], nums[pr] = nums[pr], nums[pl]
    nums[left], nums[pr] = nums[pr], nums[left]
    return pr


T = int(input())
for t in range(1, T + 1):
    nums = list(map(int, input().split()))

    quick_sort(0, len(nums) - 1)
    print(f'#{t}', *nums)
