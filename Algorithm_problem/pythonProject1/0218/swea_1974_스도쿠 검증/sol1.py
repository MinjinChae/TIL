# counting sort를 이용한 스도쿠 검증
import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
# pprint(arr)


    # # row col dat 등록
    # # 가로 확인
    for r in range(9):
        bucket_r = [0] * 10  # 버킷 만들기
        for c in range(9):
            bucket_r[arr[r][c]] += 1
            # 중복 확인
        for i in range(1, 10): # 1부터 9까지
            if bucket_r[i] != 1:
                result = 0
                break
            else:
                result = 1

    # 세로 확인
    for r in range(9):
        bucket_c = [0] * 10   # 버킷 만들기
        for c in range(9):
            bucket_c[arr[c][r]] += 1
            # 중복 확인
        for i in range(1, 10):
            if bucket_c[i] != 1:
                result = 0
                break
            else:
                result = 1

    print(result)

    # 3X3 확인
    for r in range(9,3):
        for c in range(9,3):
            bucket_x = [0] * 10
            for i in range(3):
                for j in range(3):
                    bucket_x[arr[r+i][c+j]] += 1

                    # 중복 확인
                    for k in range(1, 10):
                        if bucket_x[k] != 1:
                            result = 0
                            break
                        else:
                            result = 1
    #
    # print(f'#{tc} {result}')

