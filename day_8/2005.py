import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
# Solution 1
T = int(input())

for t in range(1, T + 1):
    N = int(input())

    print(f'#{t}')
    cur = [1]
    for i in range(N):
        print(*cur)
        cur = [1] + [cur[j] + cur[j + 1] for j in range(i)] + [1]


# Solution 2
def triangle(num: int) -> list:
    if num == 1:
        print(1)
        return [1]
    lst = triangle(num - 1)
    result = [1] + [lst[i] + lst[i + 1] for i in range(num - 2)] + [1]
    print(*result)
    return result


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    print(f'#{t}')
    triangle(N)
