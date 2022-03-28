import sys

sys.stdin = open('input.txt')

def dfs(i, cnt, total):
    global min_total  # 전역에 있는 min_total의 값을 조작해야하니까 global 선언해줘!
    # 가지치기!! -> 아직 다 더하지도 않았는데 최솟값을 넘으면 얘는 가망이 없어..
    if total >= min_total:
        return
    # 사무실로 돌아가는거 제외하고 다 돌았으면
    if cnt == N - 1:
        total += arr[i][0]  # 사무실로 돌아가는 좌표 자리값 더해줘
        min_total = min(min_total, total)

    else:
        # 자기 사무실 제외하고 가
        for j in range(1, N):
            if i != j and not visited[j]:
                visited[j] = 1
                dfs(j, cnt + 1, total + arr[i][j])
                visited[j] = 0  # 방문 기록 지워줘야해!!!


# input 받자!
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    min_total = 987654321

    dfs(0, 0 ,0)
    print(f'#{tc} {min_total}')

