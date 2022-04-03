T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for r in range(N):
        for c in range(M):
            each_sum = 0
            for i in range(K):
                for j in range(K):
                    dr = r + i
                    dc = c + j

                    if 0 <= dr < N and 0 <= dc < M:
                        each_sum += arr[dr][dc]

                        for l in range(1, K - 2):
                            for o in range(1, K - 2):
                                if 0 <= l+r < N and 0 <= o+c < M:
                                    each_sum -= arr[l+r][o+c]

            if max_sum < each_sum:
                max_sum = each_sum

    # print(arr)
    print(f'#{tc} {max_sum}')

