import sys
from collections import deque
# sys.stdin = open('input.txt')
# delta로 상 하 좌 우 탐색
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

# bfs 정의
def bfs(i, j):
    # queue를 만들어주고 deque로 형변환
    queue = deque()
    queue.append([i, j])
    while queue:  # queue가 빌 때까지 반복해
        [i, j] = queue.popleft()  # 그 다음 나오세요
        for k in range(4):
            dr = i + d_row[k]
            dc = j + d_col[k]
            # 배추 밭에서 벗어나지 않고, 배추 발견하면
            if 0 <= dr < N and 0 <= dc < M and matrix[dr][dc] == 1:
                queue.append([dr, dc])  # queue에 넣어주고
                matrix[dr][dc] = 0  # 탐색 끝났으면 0으로 바꿔줘!


T = int(input())
for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    matrix = [[0 for _ in range(M)] for _ in range(N)]

    # input 받으면서 배추 위치 넣어주기
    for _ in range(K):
        i, j = map(int, input().split())
        matrix[j][i] = 1  # x, y 바꿔서 넣어줘야해..그지같네
    cnt = 0  # 지렁이 수
    for x in range(N):  # 이것도 그지같음
        for y in range(M):
            if matrix[x][y] == 1: # 어? 배추 발견!!
                bfs(x, y)  # 주변 탐색하자
                cnt += 1  # 탐색 끝났으니까 지렁이 추가

    print(cnt)

