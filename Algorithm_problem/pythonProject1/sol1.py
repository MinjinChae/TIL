# point
# 1. 경비원은 상, 하, 좌, 우만 감시 가능!
# 2. 1에 막히면 그 이후는 모두 사각지대
# 3. 전체 - '1'구역(벽이 있는 구역) - 감시 가능 위치 - 경비원 자기 자리 = 사각지대
import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 전체 구역
    matrix = n * n

    # 벽이 있는 구역
    cnt = 0
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 1:
                cnt += 1

    # 사각지대 계산
    total = 1
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 2:
                security = arr[r][c]
            # delta 이용  상 하 좌 우
                d_row = [-1, 1, 0, 0]
                d_col = [0, 0, -1, 1]
                for i in range(4):
                    for j in range(1, n):
                        dr = r + d_row[i] * j
                        dc = c + d_col[i] * j
                        if 0 <= dr < n and 0 <= dc < n and arr[dr][dc] == 1:
                            break

                        elif 0 <= dr < n and 0 <= dc < n and arr[dr][dc] != 1:
                            total += 1

    result = matrix - cnt - total

    print(f'#{tc} {result}')


import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    
    print(f'#{tc} ')

