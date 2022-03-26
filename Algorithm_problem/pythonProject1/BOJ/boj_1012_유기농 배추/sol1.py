import sys
from collections import deque
sys.stdin = open('input.txt')

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    while queue:
        [i, j] = queue.popleft()
        for k in range(4):
            dr = i + d_row[k]
            dc = j + d_col[k]
            if 0 <= dr < N and 0 <= dc < M and matrix[dr][dc] != 0 and not visited[dr][dc]:
                queue.append([dr, dc])
                visited[dr][dc] = 1


T = int(input())
for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    visited = [[0 for _ in range(M)] for _ in range(N)]
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split())
        matrix[j][i] = 1

    cnt = 0

    for x in range(M):
        for y in range(N):
            if matrix[x][y] == 1 and not visited[x][y]:
                bfs(x, y)
                cnt += 1

    print(f'#{tc} {cnt}')

