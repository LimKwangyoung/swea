import sys

message = sys.stdin.readline().strip()
keys = sys.stdin.readline().strip()

# 5x5 table
table = []
for key in keys:
    if key not in set(table):
        table.append(key)
for i in list(range(ord('A'), ord('J'))) + list(range(ord('K'), ord('Z') + 1)):
    if chr(i) not in set(table):
        table.append(chr(i))
table = [table[i:i + 5] for i in range(0, 25, 5)]

# split the message
encode = []
idx = 0
while idx < len(message):
    if idx < len(message) - 1 and message[idx] != message[idx + 1]:
        encode.append(message[idx:idx + 2])
        idx += 2
    else:
        if idx == len(message) - 1 or message[idx] != 'X':
            encode.append(message[idx] + 'X')
        else:
            encode.append(message[idx] + 'Q')
        idx += 1

# encoding
for idx, code in enumerate(encode):
    pos_1 = pos_2 = None
    for i in range(5):
        for j in range(5):
            if code[0] == table[i][j]:
                pos_1 = [i, j]
            if code[1] == table[i][j]:
                pos_2 = [i, j]
    # row
    if pos_1[0] == pos_2[0]:
        encode[idx] = table[pos_1[0]][(pos_1[1] + 1) % 5] + table[pos_2[0]][(pos_2[1] + 1) % 5]
        continue
    # col
    if pos_1[1] == pos_2[1]:
        encode[idx] = table[(pos_1[0] + 1) % 5][pos_1[1]] + table[(pos_2[0] + 1) % 5][pos_2[1]]
        continue
    # last
    encode[idx] = table[pos_1[0]][pos_2[1]] + table[pos_2[0]][pos_1[1]]

print(''.join(encode))
