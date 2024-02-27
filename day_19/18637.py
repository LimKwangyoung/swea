import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    cards = list(map(int, input().split()))

    result = []
    p_1, p_2 = 0, 1
    cnt_1, cnt_2 = [0] * 10, [0] * 10
    while p_2 < 12:
        cnt_1[cards[p_1]] += 1
        cnt_2[cards[p_2]] += 1

        if p_1 >= 4:
            for i in range(10):
                if cnt_1[i] >= 3 or (i <= 7 and cnt_1[i] * cnt_1[i + 1] * cnt_1[i + 2] > 0):
                    result.append(1)
                    break
        if not result and p_2 >= 5:
            for i in range(10):
                if cnt_2[i] >= 3 or (i <= 7 and cnt_2[i] * cnt_2[i + 1] * cnt_2[i + 2] > 0):
                    result.append(2)
                    break
        if result:
            break
        p_1 += 2
        p_2 += 2
    print(f'#{t} {result[0] if len(result) == 1 else 0}')
