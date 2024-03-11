import sys

switches = {
    0: [0, 4, 3, 3, 4, 3, 2, 2, 1, 2],
    1: [4, 0, 5, 3, 2, 5, 6, 2, 5, 4],
    2: [3, 5, 0, 2, 5, 4, 3, 5, 2, 3],
    3: [3, 3, 2, 0, 3, 2, 3, 3, 2, 1],
    4: [4, 2, 5, 3, 0, 3, 4, 2, 3, 2],
    5: [3, 5, 4, 2, 3, 0, 1, 3, 2, 1],
    6: [2, 6, 3, 3, 4, 1, 0, 4, 1, 2],
    7: [2, 2, 5, 3, 2, 3, 4, 0, 3, 2],
    8: [1, 5, 2, 2, 3, 2, 1, 3, 0, 1],
    9: [2, 4, 3, 1, 2, 1, 2, 2, 1, 0]
}

single = [6, 2, 5, 5, 4, 5, 6, 4, 7, 6]

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(list, sys.stdin.readline().split())

    if len(A) > len(B):
        A, B = B, A    
    result = 0
    while A:
        a, b = A.pop(), B.pop()
        result += switches[int(a)][int(b)]
    while B:
        b = B.pop()
        result += single[int(b)]
    print(result)
