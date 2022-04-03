import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum1 = 0
    max_sum2 = 0

    # 1. 3x3
    for r in range(N):
        for c in range(N):
            d_sum1 = 0
            # 자기자신 위치도 넣어야해!!
            d_row = [0, -1, 1, 0, 0, -1, -1, 1, 1]
            d_col = [0, 0, 0, -1, 1, -1, 1, -1, 1]
            for k in range(len(d_row)):
                dr = r + d_row[k]
                dc = c + d_col[k]
                if 0 <= dr < N and 0 <= dc < N:
                    d_sum1 += arr[dr][dc]
                else:
                    d_sum1 = 0
                    break

            if max_sum1 < d_sum1:
                max_sum1 = d_sum1

    # 물풍선
    for r in range(N):
        for c in range(N):
            d_sum2 = 0
            d_row = [-1, 1, 0, 0]
            d_col = [0, 0, -1, 1]
            power = arr[r][c]
            d_sum2 += power
            for k in range(4):
                for p in range(1, power):
                    dr = r + d_row[k] * p
                    dc = c + d_col[k] * p
                    if 0 <= dr < N and 0 <= dc < N:
                        d_sum2 += arr[dr][dc]
            if max_sum2 < d_sum2:
                max_sum2 = d_sum2

    if max_sum1 > max_sum2:
        ans = max_sum1
    elif max_sum1 < max_sum2:
        ans = max_sum2

    print(f'#{tc} {ans}')

