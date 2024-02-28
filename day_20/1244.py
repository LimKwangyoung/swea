import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


def exchange(level: int) -> None:
    global result

    if level == cnt:
        total = int(''.join(num))
        result = max(result, total)
        return

    for i in range(N):
        for j in range(N):
            if i != j:
                num[i], num[j] = num[j], num[i]
                number = int(''.join(num))
                if number not in used:
                    used.add(number)
                    exchange(level + 1)
                # used.remove(int(''.join(num)))
                    num[i], num[j] = num[j], num[i]


T = int(input())

for t in range(1, T + 1):
    num, cnt = map(int, input().split())

    used = {num}
    arr = list(num)
    N = len(arr)

    result = 0
    exchange(level=0)
    print(f'#{t} {result}')
