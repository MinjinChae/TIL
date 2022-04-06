import sys
# deque를 라이브러리를 사용하자!
from collections import deque
sys.stdin = open('input.txt')
# 최소한의 연산 횟수 -> bfs 이용
# bfs 정의
def bfs(N):
    queue = deque()  # queue를 만들어주고 deque로 형변환
    queue.append(N)  # 처음 수 queue에 들어가세요
    visited[N] = 1  # 방문 했어요 표시
    while queue:  # queue가 빌 때까지 반복
        v = queue.popleft()  # 다음 나오세요
        for i in [v+1, v-1, v*2, v-10]:  # 사용할 수 있는 연산
            if not visited[i]:  # 방문했니? 아니라면
                queue.append(i)  # queue에 넣어주고
                visited[i] = visited[v] + 1  # 현재 연산 횟수 = 이전 값 + 1
                if i == M:  # 연산해서 M이 되었어!
                    return visited[i] - 1  # 처음 방문 기록 표시한 1 빼주기


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 몇 번 연산할지 모르니까 일단 visited 배열 많이 만들어주기!
    visited = [0] * 1000001
    print(f'#{tc} {bfs(N)}')

