import sys


def ranking(arr: list, size: int) -> list:
    result = [0] * N

    counts = [[] for _ in range(size)]
    for idx, score in arr:
        counts[score].append(idx)

    ranks = 1
    for tmp in counts[::-1]:
        if tmp:
            for idx in tmp:
                result[idx] = ranks
            ranks += len(tmp)
    return result


N = int(sys.stdin.readline())

total = [[i, 0] for i in range(N)]
for _ in range(3):
    lst = list(enumerate(map(int, sys.stdin.readline().split())))
    print(*ranking(lst, 1001))
    for key, val in lst:
        total[key][1] += val
print(*ranking(total, 3001))
