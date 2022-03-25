from collections import deque

# bfs 정의
def bfs(n):
    # queue를 deque로 형변환 해주고 처음 노드 넣어줘!
    queue = deque([n])
    visited[n] = 1  # 방문 했어요 표시
    while queue:  # queue가 빌때까지 반복해주기
        V = queue.popleft()  # 다음 나오세요
        print(V, end=' ')
        for i in graph[V]:  # 현재 노드랑 연결된 노드들 나와봐
            if not visited[i]:  # 너 방문했어?
                queue.append(i)  # 안했으면 queue에 넣어주고
                visited[i] = 1  # 방문 했어요 표시
                                # 다시 while문으로 올라가서 반복해!


# N: 정점의 수, M: 간선의 수, V: 시작할 정점의 번호
N, M, V = map(int, input().split())
# 1. 인접행렬 만들기
# matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
# 2. 인접 리스트 만들기
# -> 노드 번호를 idx로 하는 리스트 만들기
graph = [[] for _ in range(N+1)]
# 방문 기록 리스트 만들기
visited = [0 for _ in range(N+1)]
for _ in range(M):  # M줄만큼 입력 받아
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# 작은 것 먼저 방문해야해!
for _ in range(N+1):
    graph[i].sort()

bfs(V)


print(graph)
# print(visited)
# for _ in range(M):