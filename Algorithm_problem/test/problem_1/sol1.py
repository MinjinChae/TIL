import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    sum_lst = []
    for r in range(n):
        sum_num = 0
        for c in range(k):
            if r + c < n:
                sum_num += arr[r][r+c]
                sum_lst.append(sum_num)

    # bubble sort 최댓값 찾기
    for _ in range(len(sum_lst)):
        for i in range(len(sum_lst)-1):
            if sum_lst[i] > sum_lst[i+1]:
                sum_lst[i], sum_lst[i+1] = sum_lst[i+1], sum_lst[i]
                # 오름차순 정렬: sum_lst[-1]이 최댓값
    print(f'#{tc} {sum_lst[-1]}')



