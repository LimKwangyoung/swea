import sys

sys.stdin = open('input.txt')
##################################################
from itertools import combinations


def check(arr: list, candidates: tuple, medicines: str) -> bool:
    for idx in range(len(candidates)):
        arr[candidates[idx]] = [medicines[idx]] * W

    for col in range(W):
        flag = False
        vertical = ''.join([arr[row][col] for row in range(D)])

        for tmp in vertical.split('0'):
            if len(tmp) >= K:
                flag = True
                break
        else:
            for tmp in vertical.split('1'):
                if len(tmp) >= K:
                    flag = True
                    break

        if not flag:
            return False
    return True


def test() -> None:
    result = 1
    while True:
        m_lst = [bin(i)[2:].zfill(result) for i in range(2 ** result)]
        for c in combinations(range(D), result):
            for m in m_lst:
                ans = check([film.copy() for film in films], c, m)
                if ans:
                    print(f'#{t} {result}')
                    return
        result += 1


T = int(input())

for t in range(1, T + 1):
    D, W, K = map(int, input().split())
    films = [input().split() for _ in range(D)]

    if check(films, tuple(), str()):
        print(f'#{t} {0}')
    else:
        test()

# def bfs(films: list) -> int:
#     que = collections.deque([(films, 0, set(range(D)))])
#
#     while que:
#         films, cnt, used = que.popleft()
#
#         for row in list(used):
#             copied = [film.copy() for film in films]
#
#             copied[row] = ['0'] * W
#             if check(copied):
#                 print(set(range(D)) - used | {row})
#                 return cnt + 1
#             que.append((copied, cnt + 1, used - {row}))
#
#
#             copied[row] = ['1'] * W
#             if check(copied):
#                 print(set(range(D)) - used | {row})
#                 return cnt + 1
#             que.append((copied, cnt + 1, used - {row}))
#
#             print(set(range(D)) - used | {row})
#
#             # copied[row] = films[row]
#             # print(films == copied)