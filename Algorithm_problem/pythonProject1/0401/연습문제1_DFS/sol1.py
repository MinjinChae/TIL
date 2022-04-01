# dfs 정의
def dfs(v):
    visited[v] = 1  # 방문했어요 표시
    print(v, end=' ')
    for i in graph[v]:  # 현재 노드랑 연결된 노드들 나와
        if not visited[i]:  # 너 방문했어? 안했으면
            dfs(i)  # 반복해

# input 받자
graph = [[] for _ in range(8)]
visited = [0 for _ in range(8)]
for _ in range(8):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
dfs(1)
# print(graph)
# print(visited)