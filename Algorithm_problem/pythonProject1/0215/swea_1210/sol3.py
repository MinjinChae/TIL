# 출발점 반환 -> 2인 좌표에서 거꾸로 올라가기
import sys

sys.stdin = open('input.txt')

# 테스트 케이스 10개 (문제 제대로 읽어라)
T = 10
for tc in range(1, T+1):
    n = int(input())
    # 100X100 2차원 리스트 만들기
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # x 좌표 찾아주기
    # 1. x의 row idx는 99야
    # 2. x의 col idx 찾아주기
    for i in range(100):
        if ladder[99][i] == 2:
            col = i
            break  # 찾았으면 멈춰!
    row = 99

    # delta 활용
            # 상 좌 우
    d_row = [-1, 0, 0]
    d_col = [0, -1, 1]
    d = 0 # 몰라 이거 왜 해줘

    while row > 0:  # row가 0보다 클 때까지 반복(도착하면 row는 0이니까!)
        dr = row + d_row[d]
        dc = col + d_col[d]
        if 0 <= dr < 99 and 0 <= dc < 99: # index error 방지
            if ladder[dr][dc] == 1:


    print(f'#{tc} ')

