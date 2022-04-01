from collections import deque
# bfs 정의
def bfs(v):
    queue = deque()  # queue 만들어주고 deque로 형변환
    queue.append(v)  # 첫 노드 넣어줘
    visited[v] = 1  # 방문했어요 표시
    while queue:  # queue가 빌때까지 반복해주기
        v = queue.popleft()  # 다음 나오세요
        print(v, end=' ')
        for i in graph[v]:  # 현재 노드랑 연결된 노드들 나와봐
            if not visited[i]:  # 너 방문했니? 안했으면
                queue.append(i)  # 추가하고
                visited[i] = 1  # 방문 등록해

# input 받자
graph = [[] for _ in range(8)]
visited = [0 for _ in range(8)]
# print(graph)
for _ in range(8):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

bfs(1)
