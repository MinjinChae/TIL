# import sys
# # from collections import deque
# sys.stdin = open('rabbit.txt')

def bfs(x, y):
    global cnt
    queue = []
    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        [x, y] = queue.pop(0)
        if rabbit[i][2] == 1:
            dr = (x+1)*rabbit[i][3]
            dc = y
            if 0 <= dr < N and 0 <= dc < N and not visited[dr][dc]:
                queue.append([dr, dc])
                visited[dr][dc] = 1
                cnt += 1
        if rabbit[i][2] == 0:
            dr = (x-1)*rabbit[i][3]
            dc = y
            if 0 <= dr < N and 0 <= dc < N and not visited[dr][dc]:
                queue.append([dr, dc])
                visited[dr][dc] = 1
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    # N: 농장의 크기  M: 토끼 수
    N, M = map(int, input().split())
    rabbit = [list(map(int, input().split())) for _ in range(M)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0

    for i in range(M):
        start = rabbit[i][1]
        start = i, 1
        x, y = start
        bfs(x, y)


    # print(rabbit)
    # print(visited)
    print(cnt)

    # print(f'#{tc} ')

