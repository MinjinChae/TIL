# swea 2001.파리 퇴치
# delta를 이용한 파리 퇴치

import sys
f

sys.stdin = open('input2.txt')

T = 2

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0 # 최댓값 초기화



    # 내 위치(중간), 우, 하, 우하, 우상, 상, 좌상, 좌, 좌하
    d_row = [0, 0, 1, 1, -1, -1, -1, 0, 1]
    d_col = [0, 1, 0, 1, 1, 0, -1, -1, -1]



    if M == 2:  # M이 2X2일때
        # M X M (2X2)행렬이 가능한 범위
        for r in range(N - M + 1):
            for c in range(N - M + 1):
                rlt = 0  # 파리의 개수 합 초기화
                # 내 위치(중간), 우, 하, 우하
                for i in range(4):
                    dr = r + d_row[i]
                    dc = c + d_col[i]
                    rlt += arr[dr][dc]

                # 최댓값 비교
                if max_num < rlt:
                    max_num = rlt


    elif M == 3:  # M이 3X3일때
        # M X M (3X3)행렬이 가능한 범위
        # 3X3은 중간에서 시작(1,1) M X M이 각각 끝지점에 위치할 때 중간은(1,1)(1,4)(4,1)(4,4)에 위치함
        # range는 1부터 5까지
        for r in range(1, N - M + 2):
            for c in range(1, N - M + 2):
                rlt = 0 # 파리의 개수 합 초기화
                # 내 위치(중간), 우, 하, 우하, 우상, 상, 좌상, 좌, 좌하
                for i in range(9):
                    dr = r + d_row[i]
                    dc = c + d_col[i]
                    rlt += arr[dr][dc]

                # 최댓값 비교
                if max_num < rlt:
                    max_num = rlt


    print(f'#{tc} {max_num}')



