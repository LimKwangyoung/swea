import sys

nums = ''.join(sys.stdin.readline().split())

if nums == '12345678':
    print('ascending')
elif nums == '87654321':
    print('descending')
else:
    print('mixed')
