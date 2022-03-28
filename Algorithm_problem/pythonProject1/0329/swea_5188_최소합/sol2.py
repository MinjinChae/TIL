# dfs로 풀기
import sys
sys.stdin = open('input.txt')

# dfs 함수 정의
# total은 (i, j)로 이동하면서 그 자리의 수를 더해준 값
def dfs(i, j, total):
    global min_total  # 전역에 있는 min_total의 값을 조작해야하니까 global 선언해줘!
    # 가지치기!! -> 도착도 안했는데 지금까지의 합이 최소합을 넘으면 얘는 버리자..
    if total >= min_total:
        return

    if i == N - 1 and j == N - 1:  # 도착 지점에 오면
        # 지금까지의 최소합과 합을 비교해서 min_total 갱신시켜줘
        if min_total > total:
            min_total = total

    else:  # 그게 아니라면
        if i + 1 < N:  # 범위를 벗어나지 않으면 아래로 이동
            dfs(i+1, j, total + arr[i + 1][j])  # 아래로 이동하면서 그 자리의 값을 더해줘

        if j + 1 < N:  # 범위를 벗어나지 않으면 오른쪽으로 이동
            dfs(i, j+1, total + arr[i][j + 1])  # 오른쪽으로 이동하면서 그 자리의 값을 더해줘

# input 받자!
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_total = 987654321  # 최솟값 찾아줘야 하니까 비교값은 엄청 큰 수로!
    dfs(0, 0, arr[0][0])  # (0, 0)에서 출발하고 arr[0][0]의 값도 같이 함수에 넣자


    print(f'#{tc} {min_total}')

