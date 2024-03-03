import sys

sys.stdin = open('input.txt')
##################################################
import collections


def move() -> None:
    # up
    if micros[micro][3] == 1:
        micros[micro][0] -= 1
        # medicine
        if micros[micro][0] == 0:
            micros[micro][3] = 2
            micros[micro][2] //= 2
            if micros[micro][2] == 0:
                del micros[micro]
    # down
    elif micros[micro][3] == 2:
        micros[micro][0] += 1
        # medicine
        if micros[micro][0] == N - 1:
            micros[micro][3] = 1
            micros[micro][2] //= 2
            if micros[micro][2] == 0:
                del micros[micro]
    # left
    elif micros[micro][3] == 3:
        micros[micro][1] -= 1
        # medicine
        if micros[micro][1] == 0:
            micros[micro][3] = 4
            micros[micro][2] //= 2
            if micros[micro][2] == 0:
                del micros[micro]
    # right
    else:
        micros[micro][1] += 1
        # medicine
        if micros[micro][1] == N - 1:
            micros[micro][3] = 3
            micros[micro][2] //= 2
            if micros[micro][2] == 0:
                del micros[micro]


T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().strip().split())
    micros = collections.defaultdict(list)
    for i in range(K):
        micros[i] = list(map(int, input().strip().split()))

    for _ in range(M):
        for micro in micros:
            move()

        collisions = collections.defaultdict(list)
        for micro in micros:
            collisions[''.join(map(str, micros[micro][:2]))].append(micro)

        for collision in collisions:
            # merge
            if len(collisions[collision]) >= 2:
                max_micro = max_num = -1
                for micro in collisions[collision]:
                    if max_num < micros[micro][2]:
                        max_micro = micro
                        max_num = micros[micro][2]
                for micro in collisions[collision]:
                    if micro != max_micro:
                        micros[max_micro][2] += micros[micro][2]
                        del micros[micro]
    result = 0
    for micro in micros:
        result += micros[micro][2]
    print(f'#{t} {result}')
