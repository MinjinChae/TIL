import sys

sys.stdin = open('rabbit.txt')
# input 받자
T = int(input())
for tc in range(1, T + 1):
    # N: 농장 크기 M: 토끼 수
    N, M = map(int, input().split())
    # 피해를 입은 구역 체크하기 위한 matrix 생성
    matrix = [[0 for _ in range(N)]for _ in range(N)]
    for _ in range(M):  # M개의 줄
        # r, c: 행과 열  direction: 이동 방향  jump:점프 거리
        r, c, direction, jump = map(int, input().split())

    # 상 하 좌 우  0  1  2  3
        d_row = [-1, 1, 0, 0]
        d_col = [0, 0, -1, 1]
        # 농장의 거리를 벗어나지 않을 때까지 반복!
        while 0 <= r < N and 0 <= c < N:
            # 1. 일단 시작 위치에서 당근 훔쳐!
            # 2. 점프한 위치에서 당근 훔쳐!
            matrix[r][c] = 1
            # 점프한 위치로 갱신
            r = r + d_row[direction]*jump
            c = c + d_col[direction]*jump

    # 당근을 모두 훔쳤습니다... 얼마나 피해를 입었을까?
    cnt = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 1:
                cnt += 1

    print(f'#{tc} {cnt}')

