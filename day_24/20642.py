import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections


def operate(num: int) -> list:
    return [num + 1, num - 1, num * 2, num - 10]


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    result = None
    used = [0] * 1000001
    que = collections.deque([N])
    while que:
        total = que.popleft()

        for i in operate(total):
            if i == M:
                result = used[total] + 1
                break
            if not (0 < i < 1000000) or used[i]:
                continue
            que.append(i)
            used[i] = used[total] + 1

        if result:
            break
    print(f'#{t} {result}')
