import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    time = list(map(int, input().split()))

    print(f'#{tc} ')

