import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################
import collections

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, list(input()))) for _ in range(N)]

    costs = [[float('inf')] * N for _ in range(N)]
    costs[0][0] = 0
    que = collections.deque([(0, 0)])
    while que:
        row, col = que.popleft()
        coord = ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col))
        for r, c in coord:
            if 0 <= r < N and 0 <= c < N:
                tmp = costs[row][col] + graph[r][c]
                if tmp < costs[r][c]:
                    costs[r][c] = tmp
                    que.append((r, c))
    print(f'#{t} {costs[-1][-1]}')
