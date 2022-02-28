import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_lst = [] # 합들을 넣어줄 빈 리스트 만들기

    # 행의 합
    for r in range(100):
        sum_row = 0 # 한 행씩 돌고 초기화 시켜줘야해
        for c in range(100):
            sum_row += arr[r][c]
            sum_lst.append(sum_row)

    # 열의 합
    for c in range(100):
        sum_col = 0 # 한 열씩 돌고 초기화 시켜줘야해
        for r in range(100):
            sum_col += arr[r][c]
            sum_lst.append(sum_col)

    # 대각선의 합(\)
    sum_diag1 = 0
    for i in range(100):
        sum_diag1 += arr[i][i]
        sum_lst.append(sum_diag1)

    # 대각선의 합(/)
    sum_diag2 = 0
    for i in range(100):
        sum_diag2 += arr[i][99-i]
        sum_lst.append(sum_diag2)

    # sum_lst에서 최댓값 구하기
    max_num = sum_lst[0]
    for i in range(len(sum_lst)):
        if max_num <= sum_lst[i]:
            max_num = sum_lst[i]

    print(f'#{tc} {max_num}')

