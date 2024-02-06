import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt', encoding='UTF8')
##################################################


# Solution 1
def boyer_moore(pattern: str, text: str) -> int:
    result = 0
    N, M = len(text), len(pattern)

    alphabets = [M] * 256
    for i in range(M):
        alphabets[ord(pattern[i])] = M - 1 - i

    i = j = M - 1
    while i < len(text):
        if j == -1:
            result += 1
            i += 2 * M
            j = M - 1
        elif text[i] == pattern[j]:
            i -= 1
            j -= 1
        else:
            try:
                i += max(alphabets[ord(text[i])] - 1, M - j)
                j = M - 1
            except IndexError:  # 쁒
                i += max(M - 1, M - j)
                j = M - 1
    return result


for _ in range(1, 11):
    t = int(input())
    cnt = boyer_moore(input(), input())
    print(f'#{t} {cnt}')

# Solution 2
for _ in range(1, 11):
    t = int(input())
    pattern = input()
    text = input()

    print(f'#{t} {len(text.split(pattern))- 1}')
