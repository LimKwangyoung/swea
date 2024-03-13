import sys

sys.stdin.readline()
secrets = ''.join(sys.stdin.readline().split())
users = ''.join(sys.stdin.readline().split())

print('secret' if secrets in users else 'normal')