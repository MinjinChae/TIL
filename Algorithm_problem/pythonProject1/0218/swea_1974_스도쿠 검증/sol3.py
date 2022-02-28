import sys

sys.stdin = open('input.txt')

# 가로, 세로 확인 함수
def sudoku_rc(lst):
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


# 3X3 확인 함수
def sudoku_three(lst):
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            bucket_x = [0] * 10
            for i in range(3):
                for j in range(3):
                    bucket_x[lst[r + i][c + j]] += 1

            # 중복 확인
            for k in range(1, 10):
                if bucket_x[k] != 1:
                    result = 0
                    return result
                else:
                    result = 1
    return result

T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    arr_trans = list(map(list, zip(*arr)))


    if sudoku_rc(arr) and sudoku_rc(arr_trans) and sudoku_three(arr):
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')

