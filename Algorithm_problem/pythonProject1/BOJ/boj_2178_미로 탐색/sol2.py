from collections import deque

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    while queue:
        [i, j] = queue.popleft()
        # 도착지점에 오면 그만 반복해!
        if i == N - 1 and j == M - 1:
            break
        for k in range(4):
            dr = i + d_row[k]
            dc = j + d_col[k]
            # 미로 찾기 공간을 넘어가면 무시해!
            if 0 > dr or dr >= N or 0 > dc or dc >= M:
                continue
            # 이동할 수 없는 칸을 만나면 무시해!
            if arr[dr][dc] == 0:
                continue
            # 이동할 수 있고, 방문한 적이 없으면
            if arr[dr][dc] == 1 and not visited[dr][dc]:
                queue.append([dr, dc])  # queue에 추가해주고
                visited[dr][dc] = visited[i][j] + 1  # 이전 방문 기록 + 1 해줘

    ans = visited[i][j]
    return ans


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
print(bfs(0, 0))

