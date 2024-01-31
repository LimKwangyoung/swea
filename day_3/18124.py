import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
# Solution 1
T = int(input())

for t in range(1, T + 1):
    nums = list(map(int, input().split()))

    for i in range(1, 1 << 10):
        total = 0
        for j in range(10):
            if i & (1 << j):
                total += nums[j]
        if total == 0:
            print(f'#{t} 1')
            break
    else:
        print(f'#{t} 0')


# Solution 2
def subset(idx: int, num: int):
    global zero
    if zero:
        return
    if idx != 0 and num == 0:
        zero = 1
        return

    for i in range(idx, 10):
        subset(i + 1, num + nums[i])


T = int(input())

for t in range(1, T + 1):
    nums = list(map(int, input().split()))

    zero = 0
    subset(0, 0)
    print(f'#{t} {zero}')
