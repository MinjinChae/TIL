from collections import deque
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]
def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    while queue:
        [i, j] = queue.popleft()
        if i == N - 1 and j == M - 1:
            break
        for k in range(4):
            dr = i + d_row[k]
            dc = j + d_col[k]
            if 0 <= dr < N and 0 <= dc < M and arr[dr][dc] == 1 and not visited[dr][dc]:
                queue.append([dr, dc])
                visited[dr][dc] = visited[i][j] + 1

    ans = visited[i][j]
    return ans


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
print(bfs(0, 0))

