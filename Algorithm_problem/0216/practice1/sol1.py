import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    s = input()
    s = s[::-1]

    print(f'#{tc} {s}')

