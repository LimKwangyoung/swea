import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
# Solution 1
import collections

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    cheeses = list(map(int, input().split()))

    idx = N
    que = collections.deque([[num, cheese] for num, cheese in enumerate(cheeses[:idx])])
    while len(que) != 1:
        num, cheese = que.popleft()
        if cheese // 2:
            que.append([num, cheese // 2])
        elif idx < M:
            que.append([idx, cheeses[idx]])
            idx += 1
    print(f'#{t} {que.pop()[0] + 1}')

# Solution 2
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    cheeses = list(map(int, input().split()))

    idx = N
    oven = [[num, cheese] for num, cheese in enumerate(cheeses[:idx])]

    i = 0
    cnt = N
    while True:
        if not oven[i]:
            i = (i + 1) % N
            continue

        if oven[i][1] // 2:
            oven[i][1] //= 2
        else:
            if idx < M:
                oven[i] = [idx, cheeses[idx]]
                idx += 1
            else:
                if cnt == 1:
                    break
                oven[i] = None
                cnt -= 1
        i = (i + 1) % N
    print(f'#{t} {oven[i][0] + 1}')
