# 중복방문 BFS, 조건(이전 결과보다 더 나은 결과로 갱신)
from collections import deque
import sys
sys.stdin = open('input.txt')
def bfs(si, sj, ei, ej):
    queue = deque()
    queue.append([si, sj])
    visited[si][sj] = arr[si][sj] # 0
    while queue:
        ci, cj = queue.popleft()
        for k in range(4):
            d_row = [-1, 1, 0, 0]
            d_col = [0, 0, -1, 1]
            ni = ci + d_row[k]
            nj = cj + d_col[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] > visited[ci][cj] + arr[ni][nj]:
                queue.append([ni, nj])
                visited[ni][nj] = visited[ci][cj] + arr[ni][nj]
    return visited[ei][ej]



T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 지도의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 지도의 정보
    visited = [[100000 for _ in range(N)] for _ in range(N)]  # 방문 기록 체크
    ans = bfs(0, 0, N - 1, N - 1)
    print(f'#{tc} {ans}')

