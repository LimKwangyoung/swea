import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


# Solution 1
def cal_max_min(arr: list) -> tuple:
    max_idx, min_idx, max_result, min_result = 0, 0, 0, 101
    for num in range(100):
        if arr[num] > max_result:
            max_idx = num
            max_result = arr[num]
        if arr[num] < min_result:
            min_idx = num
            min_result = arr[num]
    return max_idx, min_idx, max_result, min_result


for t in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(N):
        max_i, min_i, _, _ = cal_max_min(boxes)

        boxes[max_i] -= 1
        boxes[min_i] += 1

    _, _, maximum, minimum = cal_max_min(boxes)
    print(f'#{t} {maximum - minimum}')

# Solution 2
for t in range(1, 11):
    N = int(input())
    counts = [0] * 101

    for i in map(int, input().split()):
        counts[i] += 1

    left, right = 1, 100
    for _ in range(N):
        while counts[left] == 0:
            left += 1
        while counts[right] == 0:
            right -= 1

        if left < right:
            counts[right] -= 1
            counts[right - 1] += 1
            counts[left] -= 1
            counts[left + 1] += 1
    while counts[left] == 0:
        left += 1
    while counts[right] == 0:
        right -= 1
    print(f'#{t} {right - left}')
