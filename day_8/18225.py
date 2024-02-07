import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


# Solution 1
def remove(word: str) -> int:
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return remove(word[:i] + word[i + 2:])
    return len(word)


T = int(input())

for t in range(1, T + 1):
    print(f'#{t} {remove(input())}')

# Solution 2
T = int(input())

for t in range(1, T + 1):
    stack = []
    for i in input():
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{t} {len(stack)}')
