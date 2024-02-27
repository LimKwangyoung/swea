import sys

sys.stdin = open('input.txt')
##################################################
from itertools import combinations
import collections

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')
    ingredients = collections.deque(combinations(range(N), N // 2))
    while ingredients:
        lst_A = ingredients.popleft()
        lst_B = ingredients.pop()

        synergy_A = 0
        for i, j in combinations(lst_A, 2):
            synergy_A += synergy[i][j] + synergy[j][i]
        synergy_B = 0
        for i, j in combinations(lst_B, 2):
            synergy_B += synergy[i][j] + synergy[j][i]
        result = min(result, abs(synergy_A - synergy_B))
    print(f'#{t} {result}')
