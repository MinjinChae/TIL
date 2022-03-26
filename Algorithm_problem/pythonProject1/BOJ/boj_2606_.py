from collections import deque
# input 받자
V = int(input())
E = int(input())
# 노드 번호를 idx로 하는 인접 리스트 만들기
graph = [[] for _ in range(V+1)]
# 방문 기록 리스트 만들기(1차원)
visited = [0 for _ in range(V+1)]
for _ in range(E):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# cnt 초기화 해주기
cnt = 0
# bfs 정의
def bfs(n):
    global cnt  # 함수 밖에서 cnt를 호출하면 에러나! -> 전역변수 선언해줘
    # queue 만들어서 deque로 형변환 해줘
    queue = deque()
    # 처음 노드 들어가
    queue.append(n)
    # 방문 했어요 표시
    visited[n] = 1
    while queue: # queue가 빌 때까지 반복하자
        # 다음 나오세요
        V = queue.popleft()
        # 연결된 노드들 나오세요
        for i in graph[V]:
            # 방문했어? 안했으면
            if not visited[i]:
                queue.append(i)  # queue에 추가해주고
                visited[i] = 1  # 방문 했어요 표시해줘
                cnt += 1
    return cnt

print(bfs(1))

