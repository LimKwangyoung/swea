import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(0, 10, 2):
        max_idx = min_idx = i
        for j in range(i + 1, N):
            if nums[j] > nums[max_idx]:
                max_idx = j
            elif nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[max_idx] = nums[max_idx], nums[i]
        if i == min_idx:
            min_idx = max_idx
        nums[i + 1], nums[min_idx] = nums[min_idx], nums[i + 1]
    print(f'#{t} {" ".join(map(str, nums[:10]))}')
