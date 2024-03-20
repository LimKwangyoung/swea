import sys

K, P, N = map(int, sys.stdin.readline().split())

for _ in range(N):
    K *= P
    K %= 1000000007
print(K)
