import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def dfs(idx: int, total: int, cnt: int) -> None:
    global result

    if cnt and total >= 0:
        if total == 0:
            result += 1
        return

    for i in range(idx, 10):
        dfs(i + 1, total + nums[i], cnt + 1)


nums = sorted(list(map(int, input().split())))

result = 1
dfs(0, 0, 0)
print(f'#1 {result}')
