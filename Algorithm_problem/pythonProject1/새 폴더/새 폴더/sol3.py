from collections import deque
# N: 정점의 수 , M: 줄, V: 시작 정점
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)] # 2차원 리스트 만들어주기

for _ in range(M): # M줄 입력받기
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)


print(graph)

    # print(f'#{tc} ')

