import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
#################################################
# Solution 1
T = int(input())

for t in range(1, T + 1):
    word = input()

    print(f'#{t} {1 if word == word[::-1] else 0}')

# Solution 2
T = int(input())

for t in range(1, T + 1):
    word = input()

    N = len(word)
    for i in range(N // 2):
        if word[i] != word[N - 1 - i]:
            print(f'#{t} 0')
            break
    else:
        print(f'#{t} 1')
