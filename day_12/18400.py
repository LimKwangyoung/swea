import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
# Solution 1
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    nums = input().split()

    print(f'#{t} {nums[M % N]}')

# Solution 2
import collections

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    que = collections.deque(input().split())

    while M:
        que.append(que.popleft())
        M -= 1
    print(f'#{t} {que[0]}')
