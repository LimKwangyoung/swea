import sys
from collections import deque

# Solution 1
H, K, R = map(int, sys.stdin.readline().split())

trees = [[deque(), deque()] for _ in range(2 ** (H + 1))]
for i in range(2 ** H, 2 ** (H + 1)):
    works = list(map(int, sys.stdin.readline().split()))
    trees[i] = deque(works)

result = 0
for time in range(1, R + 1):
    # root node
    if trees[1][(time + 1) % 2]:
        result += trees[1][(time + 1) % 2].popleft()
    # internal node
    for i in range(2, 2 ** H, 2):
        if trees[i][(time + 1) % 2]:
            trees[i // 2][0].append(trees[i][(time + 1) % 2].popleft())
        if trees[i + 1][(time + 1) % 2]:
            trees[i // 2][1].append(trees[i + 1][(time + 1) % 2].popleft())
    # leaf node
    for i in range(2 ** H, 2 ** (H + 1), 2):
        if trees[i]:
            trees[i // 2][0].append(trees[i].popleft())
        if trees[i + 1]:
            trees[i // 2][1].append(trees[i + 1].popleft())
print(result)

# Solution 2
H, K, R = map(int, sys.stdin.readline().split())

trees = [[[], []] for _ in range(2 ** (H + 1))]
for i in range(2 ** H, 2 ** (H + 1)):
    works = list(map(int, sys.stdin.readline().split()))
    trees[i] = works

# process for leaf nodes
for i in range(2 ** H, 2 ** (H + 1), 2):
    # left child
    trees[i // 2][0] = trees[i]
    # right child
    trees[(i + 1) // 2][1] = trees[i + 1]

# process for internal nodes
H -= 1
is_odd = True
while H:
    if is_odd:
        for i in range(2 ** H, 2 ** (H + 1), 2):
            for j in range(len(trees[i][0])):
                trees[i // 2][0].extend([trees[i][0][j], trees[i][1][j]])
                trees[(i + 1) // 2][1].extend([trees[i + 1][0][j], trees[i + 1][1][j]])
                is_odd = False
    else:
        for i in range(2 ** H, 2 ** (H + 1), 2):
            for j in range(len(trees[i][0])):
                trees[i // 2][0].extend([trees[i][1][j], trees[i][0][j]])
                trees[(i + 1) // 2][1].extend([trees[i + 1][1][j], trees[i + 1][0][j]])
                is_odd = True
    H -= 1

# complete the process
result = 0
time = H + 2
idx_1 = idx_2 = 0
while time <= R:
    if time % 2 and idx_1 < len(trees[1][0]):
        result += trees[1][0][idx_1]
        idx_1 += 1
    elif not time % 2 and idx_2 < len(trees[1][1]):
        result += trees[1][1][idx_2]
        idx_2 += 1
    time += 1
print(result)
