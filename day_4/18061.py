import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def binary_search(target: int) -> int:
    cnt = 0

    start, end = 1, P
    while start <= end:
        mid = (start + end) // 2
        cnt += 1
        if mid == target:
            return cnt
        elif mid > target:
            end = mid - 1
        else:
            start = mid + 1


T = int(input())

for t in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    cnt_a = binary_search(Pa)
    cnt_b = binary_search(Pb)

    if cnt_a < cnt_b:
        print(f'#{t} A')
    elif cnt_a > cnt_b:
        print(f'#{t} B')
    else:
        print(f'#{t} 0')
