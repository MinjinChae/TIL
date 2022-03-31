from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

def bfs(i, j):
    visited[x][y] = 1
    while queue:
        [i, j] = queue.popleft()
        d_row = [-1, 1, 0, 0]
        d_col = [0, 0, -1, 1]
        for k in range(4):
            dr = i + d_row[k]
            dc = j + d_col[k]
            if 0 <= dr < N and 0 <= dc < M and not visited[dr][dc]:
                queue.append([dr, dc])
                visited[dr][dc] = visited[i][j] + 1

queue = deque()
for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            queue.append([x, y])


def result():
    bfs(x, y)
    ans = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                return -1
            ans = max(ans, visited[i][j])
    return ans - 1

print(result())




