import sys

sys.stdin = open('input3.txt')

T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            cnt = 0
            for i in range(M):
                for j in range(M):
                    cnt += arr[r + i][c + j]
            if max_num < cnt:
                max_num = cnt


    print(f'#{tc} {max_num} ')



