import sys

sys.stdin = open('input.txt')
##################################################
import collections


def rotate(cur: int, direction: int) -> None:
    contacts = [False] * 3
    for idx in range(3):
        if magnets[idx][(index[idx] + 2) % 8] != magnets[idx + 1][(index[idx + 1] - 2) % 8]:
            contacts[idx] = True

    que = collections.deque([cur])
    visited = [0] * 4
    visited[cur] = direction
    while que:
        cur = que.popleft()
        for next in (cur - 1, cur + 1):
            if 0 <= next < 4 and not visited[next] and contacts[(cur + next) // 2]:
                visited[next] = -visited[cur]
                que.append(next)

    for idx, direction in enumerate(visited):
        if direction:
            index[idx] = (index[idx] - direction) % 8


T = int(input())

for t in range(1, T + 1):
    K = int(input())
    magnets = [input().split() for _ in range(4)]

    index = [0, 0, 0, 0]
    for _ in range(K):
        n, d = map(int, input().split())
        rotate(n - 1, d)

    total = 0
    for i in range(4):
        if magnets[i][index[i]] == '1':
            total += 2 ** i
    print(f'#{t} {total}')
