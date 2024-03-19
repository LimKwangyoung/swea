import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def dfs(idx: int, total: int, cnt: int) -> None:
    global flag

    if flag or (cnt and total >= 0):
        if total == 0:
            flag = True
        return

    for i in range(idx, 10):
        dfs(i + 1, total + nums[i], cnt + 1)


T = int(input())

for t in range(1, T + 1):
    nums = sorted(list(map(int, input().split())))

    flag = False
    dfs(0, 0, 0)
    print(f'#{t} {1 if flag else 0}')
