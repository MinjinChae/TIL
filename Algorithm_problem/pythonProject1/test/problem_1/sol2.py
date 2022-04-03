import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대값 초기화
    max_sum = 0
    for r in range(N):
        each_sum = 0
        for c in range(K):
            if r + c < N:
                each_sum += arr[r][r + c]
        # 최대값 갱신시키기
        if max_sum < each_sum:
            max_sum = each_sum

    # 최대값 출력해! 여기서 each_sum 적으면 안된다구...실수하지마!
    print(f'#{tc} {max_sum}')

