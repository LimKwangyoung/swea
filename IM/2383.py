import sys

sys.stdin = open('input.txt')
##################################################


def line_up(person_arr: list, stair_info: tuple) -> int:
    def cal_distance() -> int:
        return abs(person[0] - stair[0]) + abs(person[1] - stair[1]) + depth + 1

    stair = stair_info[:2]
    depth = stair_info[-1]

    candidates = []
    for person in person_arr:
        candidates.append(cal_distance())
    candidates.sort()

    stair = candidates[:3]
    stair_idx = 0
    for candidate in candidates[3:]:
        stair[stair_idx] = max(stair[stair_idx] + depth, candidate)
        stair_idx = (stair_idx + 1) % 3
    return max(stair) if stair else 0


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    persons = []
    stairs = []
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            if line[j] == 1:
                persons.append((i, j))
            elif line[j] > 1:
                stairs.append((i, j, line[j]))

    total_lst = []
    n = len(persons)
    for i in range(2 ** n):
        tmp = []
        for j in range(n):
            if i & (1 << j):
                tmp.append(persons[j])
        total_lst.append(tmp)

    result = float('inf')
    for lst_1 in total_lst:
        lst_2 = list(set(persons) - set(lst_1))
        result = min(result, max(line_up(lst_1, stairs[0]), line_up(lst_2, stairs[1])))
    print(f'#{t} {result}')
