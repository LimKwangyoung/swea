import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


# Solution 1
def dfs() -> int:
    result = 101

    stack = [(0, 0, K)]  # (station, count, charge remain)
    while stack:
        station, cnt, remain = stack.pop()

        if station > N:
            continue
        elif station == N and result > cnt:
            result = cnt

        for k in range(1, remain + 1):
            stack.append((station + k, cnt, remain - k))
            if station + k in stations:
                stack.append((station + k, cnt + 1, K))
    return result if result != 101 else 0


T = int(input())

for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    stations = set(list(map(int, input().split())))

    print(f'#{t} {dfs()}')

# Solution 2
T = int(input())

for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    stations = set(list(map(int, input().split())))

    cur = 0
    result = 0
    while cur < N:
        k = K
        while k > 0 and cur + k < N:
            if cur + k in stations:
                cur += k
                result += 1
                break
            k -= 1
        else:
            break
    result = 0 if k == 0 else result
    print(f'#{t} {result}')
