import sys

sys.stdin = open('input11.txt')

T = 10  # 테스트 케이스 수
for tc in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    sum_lst = []

    # 대각선 합 구하기1 (\)
    sum1 = 0
    for i in range(100):
        sum1 += arr[i][i]
    sum_lst.append(sum1)

    # 대각선 합 구하기2 (/)
    sum2 = 0
    for i in range(100):
        sum2 += arr[i][99-i]
    sum_lst.append(sum2)

    # 행의 합 구하기
    for i in range(100):
        sum3 = 0
        for j in range(100):
            sum3 += arr[i][j]
        sum_lst.append(sum3)

    # 열의 합 구하기
    for j in range(100):
        sum4 = 0
        for i in range(100):
            sum4 += arr[i][j]
        sum_lst.append(sum4)

    # 최댓값 구하기
    max_num = sum_lst[0]
    for i in range(len(sum_lst)):
        if max_num < sum_lst[i]:
            max_num = sum_lst[i]

    print(f'#{tc} {max_num}')

