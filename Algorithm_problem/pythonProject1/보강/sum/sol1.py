import sys

sys.stdin = open('input.txt')

T = int(input())
arr = [list(map(int, input().split())) for _ in range(100)]

for tc in range(1, T + 1):
    for r in range(100):
        sum_row = 0
        for c in range(100):
            sum_row += arr[r][c]

    for c in range(100):
        
    print(f'#{tc} ')

