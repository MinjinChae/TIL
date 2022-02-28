import sys

sys.stdin = open('input.txt')

# 입력 받기
T = int(input())
for tc in range(1, T + 1):
    n, p = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 1. 상하좌우 바이러스 퇴치
    max_virus1 = 0
    sum_virus1 = 0
    # 위치 지정
    for r in range(n):
        for c in range(n):
            sum_virus1 = arr[r][c] # 폭탄 투하 위치에 있는거 더해주기(r,c)
            # delta   상 하 좌 우
            d_row = [-1, 1, 0, 0]
            d_col = [0, 0, -1, 1]
            for i in range(4):
                for j in range(1, p+1):
                    dr = r + d_row[i] * j
                    dc = c + d_col[i] * j
                    if 0 <= dr < n and 0 <= dc < n:
                        sum_virus1 += arr[dr][dc]
                    else:
                        continue
            if max_virus1 <= sum_virus1:
                max_virus1 = sum_virus1

    # 2. 대각선 바이러스 퇴치
    max_virus2 = 0
    sum_virus2 = 0
    for r in range(n):
        for c in range(n):
            sum_virus2 = arr[r][c]  # 폭탄 투하 위치에 있는거 더해주기(r,c)
            # delta  좌상 우상 우하 좌하
            d_row = [-1, -1, 1, 1]
            d_col = [-1, 1, -1, 1]
            for i in range(4):
                for j in range(1, p+1):
                    dr = r + d_row[i] * j
                    dc = c + d_col[i] * j
                    if 0 <= dr < n and 0 <= dc < n:
                        sum_virus2 += arr[dr][dc]
                    else:
                        continue
            if max_virus2 <= sum_virus2:
                max_virus2 = sum_virus2

    # 최댓값 구하기
    rlt = max(max_virus1, max_virus2)


    print(f'#{tc} {rlt}')

