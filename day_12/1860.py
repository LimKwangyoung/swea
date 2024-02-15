import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
# Solution 1
import collections

T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    que = collections.deque(map(int, input().split()))

    time = fish = 0
    while que and fish >= 0:
        if time and not time % M:
            fish += K

        wait = len(que)
        for _ in range(wait):
            client = que.popleft()
            if time == client:
                fish -= 1
            else:
                que.append(client)
        time += 1

    print(f'#{t} {"Possible" if fish >= 0 else "Impossible"}')

# Solution 2
T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    clients = list(map(int, input().split()))

    counts = [0] * 11112
    for client in clients:
        counts[client] += 1

    fish = 0
    for time in range(11112):
        if time and not time % M:
            fish += K
        if counts[time]:
            fish -= 1
            if fish < 0:
                print(f'#{t} Impossible')
                break
    else:
        print(f'#{t} Possible')
