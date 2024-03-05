from itertools import combinations

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    houses = [list(map(int, input().split())) for _ in range(N)]

    distances = []
    for row in range(-15, 16):
        for col in range(-15, 16):
            tmp = []  # 충전소 위치
            for idx, house in enumerate(houses):
                if row == house[0] and col == house[1]:
                    break
                dist = abs(row - house[0]) + abs(col - house[1])
                tmp.append(dist)
            else:
                distances.append(tmp)

    result = float('inf')
    for dist in distances:
        for i in range(N):
            if dist[i] > houses[i][2]:
                break
        else:
            result = min(result, sum(dist))

    if result != float('inf'):
        print(f'#{t} {result}')
    else:
        result = float('inf')
        for dist_1, dist_2 in combinations(distances, 2):
            for i in range(N):
                if dist_1[i] > houses[i][2] and dist_2[i] > houses[i][2]:
                    break
            else:
                tmp = 0
                for j in range(N):
                    tmp += min(dist_1[j], dist_2[j])
                result = min(result, tmp)

        if result != float('inf'):
            print(f'#{t} {result}')
        else:
            print(f'#{t} -1')
