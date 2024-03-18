import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def merge_sort(arr: list) -> list:
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(arr_1: list, arr_2: list) -> list:
    global cnt

    result = []
    idx_1 = idx_2 = 0
    while idx_1 < len(arr_1) and idx_2 < len(arr_2):
        if arr_1[idx_1] < arr_2[idx_2]:
            result.append(arr_1[idx_1])
            idx_1 += 1
        else:
            result.append(arr_2[idx_2])
            idx_2 += 1
    if idx_1 < len(arr_1):
        result.extend(arr_1[idx_1:])
    else:
        result.extend(arr_2[idx_2:])

    if arr_1[-1] > arr_2[-1]:
        cnt += 1
    return result


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    cnt = 0
    sorted_lst = merge_sort(nums)
    print(f'#{t} {sorted_lst[N // 2]} {cnt}')
