import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    students = [list(map(int, input().split())) for _ in range(N)]

    halls = [0] * 200
    for left, right in students:
        if left > right:
            left, right = right, left
        left = (left - 1) // 2
        right = (right - 1) // 2

        for i in range(left, right + 1):
            halls[i] += 1

    result = 0
    for i in halls:
        if i > result:
            result = i
    print(f'#{t} {result}')
