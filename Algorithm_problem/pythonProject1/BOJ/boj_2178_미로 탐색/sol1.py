from collections import deque

# delta 활용 -> 상 하 좌 우
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

# bfs 정의
def bfs(i, j):
    # queue를 deque로 형변환 해주고 처음 노드 넣어줘!
    queue = deque([[i, j]])
    # 방문 했어요 표시해줘
    visited[i][j] = 1
    while queue:  # queue가 빌때까지 반복하자
        [i, j] = queue.popleft()  # 다음 나오세요
        # 도착지점에 오면 더이상 반복하지마!
        if i == N - 1 and j == M - 1:
            break

        for k in range(4):  # 현재 위치에서 네 방향으로 위치 이동
            dr = i + d_row[k]
            dc = j + d_col[k]

            # 미로 찾기 공간 벗어나지 않고, 이동할 수 있고, 방문한 적이 없으면
            if 0 <= dr < N and 0 <= dc < M and arr[dr][dc] == 1 and not visited[dr][dc]:
                queue.append([dr, dc])  # queue에 추가해줘
                visited[dr][dc] = visited[i][j] + 1  # 이전 방문 정보에 +1

    ans = visited[i][j]
    return ans


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

print(bfs(0, 0))


