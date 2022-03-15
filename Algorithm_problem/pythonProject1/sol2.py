import sys
sys.stdin = open('sample.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    graph = [[0] for _ in range(n)]

# def bfs(v, graph):
start = arr[0][0]

# delta 이용 -> 상 하 좌 우
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
for i in range(4):
    nx = dx[i]
    ny = dy[i]

cnt = 0
if nx >= 0 or nx < n or ny >= 0 or ny < n:
    continue
if arr[nx][ny] == 1:
    cnt += 1
    while arr[nx][ny] == abs(-1):
        cnt += 1
# return cnt

# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     graph = [[0] for _ in range(n)]
    print(f'#{tc} {cnt}')


