import sys
from collections import deque
sys.stdin = open('input.txt')
# delta 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # deque 라이브러리 사용
    queue = deque()
    queue.append([x, y])

    # queue가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 상,하,좌,우 이동해
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간에서 벗어나지 않았을 경우(index error 방지)
            if 0 <= nx < n and 0 <= ny < n:
                # 탐색한 좌표가 통로이고 방문 기록이 0이면
                if maze[nx][ny] == 0 and visited[nx][ny] == 0:
                    # 이동한 거리 = 이전 값 + 1
                    visited[nx][ny] = visited[x][y] + 1
                    # queue에 추가해주기
                    queue.append([nx, ny])
                # 탐색한 좌표가 3이면(도착지점)
                elif maze[nx][ny] == 3:
                    # 지금까지 이동한 거리 반환해
                    return visited[x][y]

    # 통로를 찾을 수 없다면 0 반환해
    return 0

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    # 방문 기록 리스트 생성
    visited = [[0] * n for _ in range(n)]

    # 출발점 찾기
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                x, y = i, j

    print(f'#{tc} {bfs(x, y)}')

