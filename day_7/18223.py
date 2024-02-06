import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
#################################################
import collections

# Solution 1
T = int(input())

for t in range(1, T + 1):
    str1, str2 = input(), input()

    result = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if cnt > result:
            result = cnt
    print(f'#{t} {result}')

# Solution 2
T = int(input())

for t in range(1, T + 1):
    str1, str2 = input(), input()

    for word, freq in collections.Counter(list(str2)).most_common():
        if word in set(str1):
            print(f'#{t} {freq}')
            break
