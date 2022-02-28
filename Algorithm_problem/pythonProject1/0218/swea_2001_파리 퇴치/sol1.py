# delta를 이용한 파리 퇴치

import sys
from pprint import pprint

sys.stdin = open('input.txt')

T = 1
for tc in range(1, T + 1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0  # 최댓값 초기화

    # M X M 행렬이 가능한 범위
    for r in range(N - M + 1):
        for c in range(N - M + 1):

            d_row = [0, 0, 1, 1]  # 내 위치, 오른쪽, 아래, 오른쪽 대각선 tc 밖으로!
            d_col = [0, 1, 0, 1]  # 내 위치, 오른쪽, 아래, 오른쪽 대각선

            rlt = 0  # 파리의 개수 합 초기화

            for i in range(4): # (r,c)에 더해줘서 내 위치, 오른쪽, 아래, 오른쪽 대각선 찾아주기
                dr = r + d_row[i]
                dc = c + d_col[i]

                rlt += arr[dr][dc]  # rlt에 파리의 개수 더하기

            if max_num < rlt:
                max_num = rlt


    print(f'#{tc} {max_num}')

