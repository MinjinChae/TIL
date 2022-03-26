import sys
from collections import deque
sys.stdin = open('input.txt')

# delta 활용 -> 상 하 좌 우
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

# bfs 정의
def bfs(i, j):
    # queue 만들어서 deque 형변환 해주기
    queue = deque()
    # queue에 첫 노드 넣어주기
    queue.append([i, j])
    # 방문했으니까 1
    visited[i][j] = 1
    # queue가 빌 때까지 반복해!
    while queue:
        # 아까 넣었던 애들 나와봐
        [i, j] = queue.popleft()
        # 상하좌우 탐색하기
        for k in range(4):
            dr = i + d_row[k]
            dc = j + d_col[k]
            # 미로 찾기 공간에서 벗어나지 않고, 벽이 아니어야 하고, 방문 기록이 없으면
            if 0 <= dr < N and 0 <= dc < N and arr[dr][dc] != 1 and not visited[dr][dc]:
                queue.append([dr, dc])  # queue에 추가해줘
                visited[dr][dc] = visited[i][j] + 1  # 이전 방문 기록에 + 1
                if arr[dr][dc] == 3:  # 탐색한 좌표가 3이면 (도착했으면!)
                    ans = visited[i][j] - 1  # 출발 기록을 빼주고
                    return ans  # 지금까지 이동한 거리를 반환해!
    return 0  # 경로가 없으면 0을 반환해

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]


    # 출발점 찾기
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 2:
                i, j = x, y

    print(f'#{tc} {bfs(i, j)}')
