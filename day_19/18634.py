import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def consume(start: int, total) -> None:
    global result

    if len(path) == N:
        result = min(result, total + battery[start][0])
        return

    for i in range(N):
        if i not in path:
            path.add(i)
            consume(i, total + battery[start][i])
            path.remove(i)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')
    path = {0}
    consume(0, 0)
    print(f'#{t} {result}')
