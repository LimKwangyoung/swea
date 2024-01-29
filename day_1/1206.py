import sys

sys.stdin = open('1206_input.txt')
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


for t in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    result = [0] * N
    for i in range(2, N - 2):
        result[i] = cal_max([0, buildings[i] - cal_max([buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2]])])
    print(f'#{t} {cal_sum(result)}')
