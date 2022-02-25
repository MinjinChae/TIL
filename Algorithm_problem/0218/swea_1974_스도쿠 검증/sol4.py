import sys

sys.stdin = open('input.txt')

def sudoku_rc(lst):
    for r in range(9):
        bucket_rc = [0] * 10
        for c in range(9):
            bucket_rc[lst[r][c]] += 1
        for k in range(1, 10):
            if bucket_rc[k] != 1:
                result = 0
                return result
            else:
                result = 1
    return result

def bythree(lst):
    for r in range(0,9,3):
        for c in range(0,9,3):
            bucket_th = [0] * 10
            for i in range(3):
                for j in range(3):
                    bucket_th[lst[r+i][c+j]] += 1

            for k in range(1,10):
                if bucket_th[k] != 1:
                    result = 0
                    return result
                else:
                    result = 1
    return result


T = int(input())


for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    arr_trans = list(map(list, zip(*arr)))

    if sudoku_rc(arr) and sudoku_rc(arr_trans) and bythree(arr):
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')

