# 답이 다르게 나온다ㅠㅠ엉엉..
import sys
# deque를 라이브러리를 사용하자!
from collections import deque
sys.stdin = open('input.txt')

def bfs(i, j):
    global rlt
    queue = deque()  # queue를 만들어주고 deque로 형변환
    queue.append([i, j])  # 처음 위치 queue에 들어가세요
    visited[i][j] = 1  # 방문 했어요 표시
    while queue:  # queue가 빌 때까지 반복
        i, j = queue.popleft()  # 다음 나오세요
        # delta 활용
        d_row = [-1, 1, 0, 0]
        d_col = [0, 0, -1, 1]
        # 상하좌우로 이동해요
        for k in range(4):
            dr = i + d_row[k]
            dc = j + d_col[k]
            # 범위 안에 있고 방문하지 않았으면
            if 0 <= dr < N and 0 <= dc < N and not visited[dr][dc]:
                visited[dr][dc] = 1  # 방문 했어요 표시하고

                # 더 높은 곳으로 이동했다면
                if arr[dr][dc] > arr[i][j]:
                    # 높이 차이 만큼 연료에 더해줘
                    rlt += arr[dr][dc] - arr[i][j]
                    # 이동한 좌표 queue에 넣어줘
                    queue.append([dr, dc])
                else:  # 그게 아니라면
                    rlt += 1  # 이동할 때 기본 연료 1 더해줘
                    # 이동한 좌표 queue에 넣어줘
                    queue.append([dr, dc])


T = int(input())
for tc in range(1, T + 1):
    # 표의 가로, 세로 칸수
    N = int(input())
    # 높이가 나와있는 표
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 방문 기록 표시해 줄 visited 배열
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 연료 양
    rlt = 0
    # 좌표(0,0)에서 출발해요
    bfs(0, 0)
    print(f'#{tc} {rlt}')

