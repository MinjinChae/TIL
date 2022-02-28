import sys

sys.stdin = open('input.txt')

T = int(input())
arr = [list(map(int, input().split())) for _ in range(9)]
# pprint(arr)

for tc in range(1, T + 1):

    # 가로 확인 함수
    def sudoku_row(lst):
        # row col dat 등록
        for r in range(9):
            bucket_r = [0] * 10  # 버킷 만들기
            for c in range(9):
                bucket_r[lst[r][c]] += 1
                # 중복 확인
            for i in range(1, 10):  # 1부터 9까지
                if bucket_r[i] != 1:
                    result = 0
                    return result
                else:
                    result = 1
        return result


    # 세로 확인 함수
    def sudoku_col(lst):
        for r in range(9):
            bucket_c = [0] * 10  # 버킷 만들기
            for c in range(9):
                bucket_c[lst[c][r]] += 1
                # 중복 확인
            for i in range(1, 10):
                if bucket_c[i] != 1:
                    result = 0
                    return result
                else:
                    result = 1
            return result


    # 3X3 확인 함수
    def sudoku_three(lst):
        for r in range(9, 3):
            for c in range(9, 3):
                bucket_x = [0] * 10
                for i in range(3):
                    for j in range(3):
                        bucket_x[lst[r+i][c+j]] += 1

                # 중복 확인
                for k in range(1, 10):
                    if bucket_x[k] != 1:
                        result = 0
                        return result
                    else:
                        result = 1
                return result

    if sudoku_row(arr) and sudoku_col(arr) and sudoku_three(arr):
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')





    # print(f'#{tc} ')

