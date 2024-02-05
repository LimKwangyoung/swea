import sys

sys.stdin = open(f'{__file__.split("/")[-1][:-3]}_input.txt')
#################################################
num_dic = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
           'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
word_dic = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR',
            5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}

T = int(input())

for t in range(1, T + 1):
    tk, N = input().split()
    words = input().split()

    counts = [0] * int(N)
    for i in words:
        counts[num_dic[i]] += 1

    print(tk)
    for i in range(10):
        while counts[i] > 0:
            print(word_dic[i], end=' ')
            counts[i] -= 1
    print()
