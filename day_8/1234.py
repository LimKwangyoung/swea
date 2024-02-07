import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
##################################################


# Solution 1
def remove(word: str) -> str:
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return remove(word[:i] + word[i + 2:])
    return word


for t in range(1, 11):
    N, password = input().split()

    print(f'#{t} {remove(password)}')


# Solution 2
for t in range(1, 11):
    N, password = input().split()

    stack = []
    for i in password:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{t} {"".join(stack)}')
