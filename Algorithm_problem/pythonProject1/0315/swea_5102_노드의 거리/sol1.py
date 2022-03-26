import sys
from collections import deque
sys.stdin = open('input.txt')
# bfs 정의
def bfs(n):
    # queue 만들어서 deque로 형변환
    queue = deque()
    # queue에 첫 노드 넣어주기
    queue.append(n)
    # 방문 했어요 표시
    visited[n] = 1

    while queue:  # queue가 빌 때까지 반복하기
        v = queue.popleft()  # 다음 나오세요
        for i in graph[v]:  # 연결된 노드들 나와봐
            if not visited[i]:  # 너 방문했어?
                queue.append(i)  # 안했으면 queue에 추가하고
                visited[i] = visited[v] + 1  # 이전 방문 정보에 +1 해줘

    if visited[G]:  # G 노드의 방문 기록이 있으면
        return visited[G] - 1  # 처음 노드에 방문기록 1한거 빼주고 반환해
    else:  # 그게 아니라면
        return visited[G]  # 그냥 그대로 반환해(어차피 0이니까)


T = int(input())
for tc in range(1, T + 1):
    # V: 노드 개수 E: 간선 개수
    V, E = map(int, input().split())
    # 노드 번호를 idx로 하는 인접 리스트 만들기
    graph = [[] for _ in range(V+1)]
    # 방문 기록 리스트 만들기(1차원)
    visited = [0 for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)
    # S: 출발 노드 G: 도착 노드
    S, G = map(int, input().split())


    print(f'#{tc} {bfs(S)}')

