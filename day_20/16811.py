import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    lst = [0] * 31
    for carrot in carrots:
        lst[carrot] += 1
    counts = [num for num in lst if num]

    result = float('inf')
    for i in range(1, N - 1):
        if not (1 <= sum(counts[:i]) <= N // 2):
            break
        box_1 = sum(counts[:i])
        for j in range(i, N):
            box_2 = sum(counts[i:j])
            box_3 = sum(counts[j:])
            if 1 <= box_2 <= N // 2 and 1 <= box_3 <= N // 2:
                boxes = [box_1, box_2, box_3]
                result = min(result, max(boxes) - min(boxes))
    print(f'#{t} {-1 if result == float("inf") else result}')
