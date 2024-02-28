import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections

T = int(input())

for t in range(1, T + 1):
    num, K = input().split()

    arr = list(map(int, num))
    K = int(K)
    num_set = sorted(list(set(arr)))

    idx = 0
    max_idx = -1
    maximum = sorted(arr, reverse=True)
    while K > 0:
        if arr == maximum:
            if K % 2:
                index = collections.defaultdict(list)
                for i, n in enumerate(arr):
                    index[n].append(i)
                for key, value in index.items():
                    if len(value) >= 2:
                        break
                else:
                    arr[-1], arr[-2] = arr[-2], arr[-1]
            break
        if arr[idx] >= num_set[max_idx]:
            idx += 1
            max_idx -= 1
            continue

        index = collections.defaultdict(list)
        for i, n in enumerate([None] * idx + arr[idx:]):
            index[n].append(i)

        tmp = max(0, len(index[num_set[max_idx]]) - K)
        change_idx = index[num_set[max_idx]][tmp]
        arr[idx], arr[change_idx] = arr[change_idx], arr[idx]
        idx += 1

        if idx >= len(index[num_set[max_idx]]):
            max_idx -= 1
        K -= 1
    print(f'#{t} {"".join(map(str, arr))}')
