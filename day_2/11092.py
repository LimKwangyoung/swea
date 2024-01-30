import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def cal_max_min(arr: list, n: int) -> tuple:
    max_idx, min_idx, max_result, min_result = 0, 0, 0, 11
    for num in range(n):
        if arr[n - 1 - num] > max_result:
            max_idx = n - 1 - num
            max_result = arr[n - 1 - num]
        if arr[num] < min_result:
            min_idx = num
            min_result = arr[num]
    return max_idx, min_idx, max_result, min_result


def cal_abs(num: int) -> int:
    if num >= 0:
        return num
    else:
        return -1 * num


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_i, min_i, _, _ = cal_max_min(nums, N)
    print(f'#{t} {cal_abs(max_i - min_i)}')
