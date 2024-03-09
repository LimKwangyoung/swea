N = int(input())
nums = list(map(int, input().split()))

minimum = [[0] * (N + 1) for _ in range(N)]
for i in range(N - 1):
    for j in range(N - 1, i, -1):
        minimum[i][j] += minimum[i][j + 1]
        if nums[i] > nums[j]:
            minimum[i][j] += 1

result = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        if nums[i] < nums[j]:
            result += minimum[i][j + 1]
print(result)
