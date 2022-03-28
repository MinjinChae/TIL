# bfs로 풀기
import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(i, j, total):
    global min_total
    queue = deque()
    queue.append([i, j])
    total += arr[i][j]

    # visited[i][j] = 1
    while queue:
        [i, j] = queue.popleft()
        if i == N - 1 and j == N - 1:

            if min_total > total:
                min_total = total

            return

        else:
            if i + 1 < N:
                bfs(i+1, j, total)

            if j + 1 < N:
                bfs(i, j+1, total)


            # d_row = [0, 1]
            # d_col = [1, 0]
            # for k in range(2):
            #     dr = i + d_row[k]
            #     dc = j + d_col[k]
            #     if 0 <= dr < N and 0 <= dc < N and not visited[dr][dc]:
            #         queue.append([dr, dc])
            #         visited[dr][dc] = 1
            #         total += arr[dr][dc]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # visited = [[0 for _ in range(N)] for _ in range(N)]
    min_total = 987654321
    # total = 0
    bfs(0, 0, 0)

    # print(visited)
    # print(arr)
    print(f'#{tc} {min_total}')

