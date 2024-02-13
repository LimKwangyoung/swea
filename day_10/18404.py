import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def dfs(idx: int, total: int) -> None:
    global result

    total += idx
    if total > 10:
        return
    elif total == 10:
        result += 1
        return

    for i in range(idx + 1, 11):
        dfs(i, total)


result = 0
dfs(0, 0)
print(f'#1 {result}')
