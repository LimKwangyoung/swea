import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
#################################################
T = int(input())

for t in range(1, T + 1):
    grids = [[] for _ in range(3)]
    verticals = [[] for _ in range(9)]
    flag = True
    for i in range(9):
        lst = input().split()
        if not flag:
            continue

        # horizon
        if len(set(lst)) != 9:
            flag = False
            continue

        # vertical
        for j in range(9):
            verticals[j].append(lst[j])

        # 3x3 grid
        for j in range(3):
            grids[j] += lst[3 * j:3 * j + 3]
        if i % 3 == 2:
            for grid in grids:
                if len(set(grid)) != 9:
                    flag = False
                    continue
            else:
                grids = [[] for _ in range(3)]
    if not flag:
        print(f'#{t} {0}')
        continue

    for j in verticals:
        if len(set(j)) != 9:
            print(f'#{t} 0')
            break
    else:
        print(f'#{t} 1')
