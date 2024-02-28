import sys

sys.stdin = open('input.txt')
##################################################
import collections

T = int(input())

for t in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    receptions_time = list(map(int, input().split()))
    repairs_time = list(map(int, input().split()))
    clients = list(map(int, input().split()))

    receptions = receptions_time[:]
    repairs = repairs_time[:]
    time = clients[0]
    while True:
        