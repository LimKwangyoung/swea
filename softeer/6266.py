import sys
import collections


def check(arr: list) -> list:
    result = []
    time = 9
    for start, end in arr:
        if time != start:
            result.append(f'{time:02d}-{start:02d}')
        time = end
    if time != 18:
        result.append(f'{time:02d}-18')
    return result


N, M = map(int, input().split())

rooms = sorted([input() for _ in range(N)])
reservations = collections.defaultdict(list)
for _ in range(M):
    room, *times = input().split()
    reservations[room].append(list(map(int, times)))

for key in reservations:
    reservations[key].sort()

for i, room in enumerate(rooms):
    ans = check(reservations[room])
    print(f'Room {room}:')
    if not ans:
        print('Not available')
    else:
        print(f'{len(ans)} available:')
        print('\n'.join(map(str, ans)))
    if i != N - 1:
        print('-----')
