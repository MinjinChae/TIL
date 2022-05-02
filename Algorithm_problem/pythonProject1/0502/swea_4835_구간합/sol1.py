import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # N: 정수 개수 M: 구간합 M개
    N, M = map(int, input().split())
    # number_lst: 배열 V
    number_lst = list(map(int, input().split()))
    sum_lst = []  # 합을 넣어줄 빈 리스트 생성

    # 범위 -> 덧셈을 시작할 첫번째 idx
    for i in range(N - M + 1):
        total = 0  # total 0으로 초기화
        # i부터 i+M까지(M만큼의 구간)
        for j in range(i, i + M):
            total += number_lst[j]
        # j가 끝나면 -> 구간 하나가 끝나면 리스트에 합 넣어주기
        sum_lst.append(total)

    # max, min 사용 -> 구간의 최대합 - 최소합
    rlt = max(sum_lst) - min(sum_lst)
    print(f'#{tc} {rlt}')

