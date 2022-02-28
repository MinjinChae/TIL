# 1. 시작점을 찾아야함 -> 거꾸로 올라가야해  -> x = 시작점으로
# 2. 도착하면 row는 0이 되어야함
# 3. 좌, 우, 상 으로 이동함(델타 활용하기!)
import sys

sys.stdin = open('input.txt')

T = 10 # 테스트 케이스는 10개


for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]  # 100x100 만들기

    # 도착지점(x)의 col idx 찾기
    for col in range(100):
        if arr[99][col] == 2:
            # col = i
            break
    # 도착지점(x)의 row idx 찾기
    row = 99
    dr = (0, 0, -1) # 움직이는 방향은 좌, 우, 상
    dc = (-1, 1, 0) # 좌, 우, 상
    direction = 0

    while row > 0: # row가 0이 될때까지 반복해서 올라가야해
        new_r = row + dr[direction]
        new_c = col + dc[direction]
        if 0 <= new_r < 100 and 0 <= new_c < 100: # out of idx error 방지
            if arr[new_r][new_c] == 1: # 1이 있으면 이동!
                row = new_r  # 이동했으니까 위치 업데이트
                col = new_c  # 이동했으니까 위치 업데이트
                arr[new_r][new_c] = 0 # 이동했는데 다시 옆에 1이 있으면 다시 되돌아와서 무한루프에 빠질 수 있으니까 0으로 만들어버리기
        direction = (direction + 1) % 3
    print(f'#{tc} {col}')

