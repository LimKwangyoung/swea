import sys

sys.stdin = open(f'input.txt')
##################################################
import heapq


def check(x1: int, y1: int, direction_1: int, x2: int, y2: int, direction_2: int):
    if x1 == x2:
        if (y1 > y2 and direction_1 == 1 and direction_2 == 0) or (y1 < y2 and direction_1 == 0 and direction_2 == 1):
            return abs(y1 - y2)
    elif y1 == y2:
        if (x1 > x2 and direction_1 == 2 and direction_2 == 3) or (x1 < x2 and direction_1 == 3 and direction_2 == 2):
            return abs(x1 - x2)
    elif abs(x1 - x2) == abs(y1 - y2):
        if (x1 > x2 and
            ((y1 > y2 and ((direction_1 == 2 and direction_2 == 0) or (direction_1 == 1 and direction_2 == 3))) or
             (y1 < y2 and ((direction_1 == 0 and direction_2 == 3) or (direction_1 == 2 and direction_2 == 1))))) or \
                (x1 < x2 and
                 ((y1 > y2 and ((direction_1 == 3 and direction_2 == 0) or (direction_1 == 1 and direction_2 == 2))) or
                  (y1 < y2 and ((direction_1 == 0 and direction_2 == 2) or (direction_1 == 3 and direction_2 == 1))))):
            return abs(x1 - x2) + abs(y1 - y2)
    return False


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    distances, atoms = [], []
    for num_2 in range(N):
        x, y, direction, energy = map(int, input().split())

        for num_1, (i, j, d, e) in enumerate(atoms):
            ans = check(x, y, direction, i, j, d)
            if ans:
                distances.append((ans, num_1, num_2))
        atoms.append((x, y, direction, energy))

    heapq.heapify(distances)
    result = prev = 0
    while distances:
        dist, num_1, num_2 = heapq.heappop(distances)
        if atoms[num_1] and atoms[num_2]:
            result += atoms[num_1][3] + atoms[num_2][3]
            atoms[num_1] = atoms[num_2] = None
            prev = dist
        elif atoms[num_1] and not atoms[num_2]:
            if prev == dist:
                result += atoms[num_1][3]
                prev = dist
                atoms[num_1] = None
        elif not atoms[num_1] and atoms[num_2]:
            if prev == dist:
                result += atoms[num_2][3]
                prev = dist
                atoms[num_2] = None
    print(f'#{t} {result}')
