import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_num1 = 0
    max_num2 = 0

    # 1) 3X3 배열
    for r in range(n):
        for c in range(n):

            d_row = [0, -1, 1, 0, 0, -1, 1, -1, 1]
            d_col = [0, 0, 0, -1, 1, -1, 1, 1, -1]
            d_sum1 = 0

            for i in range(len(d_row)):
                dr = r + d_row[i]
                dc = c + d_col[i]

                if 0 <= dr < n and 0 <= dc < n:
                    d_sum1 += arr[dr][dc]
                else:
                    d_sum1 = 0
                    break

            #  최댓값 찾기
            if max_num1 < d_sum1:
                max_num1 = d_sum1

    # 2) cross 배열
    for r in range(n):
        for c in range(n):
            d_row = [-1, 1, 0, 0]
            d_col = [0, 0, -1, 1]
            d_sum2 = 0
            power = arr[r][c]
            d_sum2 += power  # 기준이 되는 자기자신을 더해줘야해

            for i in range(4):
                for p in range(1, power):
                    dr = r + d_row[i] * p
                    dc = c + d_col[i] * p

                    if 0 <= dr < n and 0 <= dc < n:
                        d_sum2 += arr[dr][dc]

            #  최댓값 찾기
            if max_num2 < d_sum2:
                max_num2 = d_sum2


    # 3) 3X3과 cross의 최댓값 비교
    if max_num1 > max_num2:
        result = max_num1
    elif max_num2 > max_num1:
        result = max_num2


    print(f'#{tc} {result} ')

