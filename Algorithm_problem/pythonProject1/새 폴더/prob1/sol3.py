import sys

sys.stdin = open('rabbit.txt')

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())  # 테스트 케이스
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # N * N matrix
    matrix = [[0] * N for _ in range(N)]

    # 각각의 토끼들을 뛰놀게 하자
    for _ in range(M):
        r, c, direction, jump = map(int, input().split())

        # 각 토끼가 같은 방향으로 계속 뛰어넘기(파먹기)
        while r >= 0 and r < N and c >= 0 and c < N:
            matrix[r][c] = 1  # 당근 먹어

            # 자, 이제 점프해
            r = r + dr[direction] * jump
            c = c + dc[direction] * jump

    # 정답 도출
    cnt = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c]:
                cnt += 1

    print(f"#{tc} {cnt}")

