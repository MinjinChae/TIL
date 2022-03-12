# 출발점 반환 -> 2인 좌표에서 거꾸로 올라가기
import sys
from pprint import pprint
sys.stdin = open('input.txt')
# 테스트 케이스 10개 (문제 제대로 읽어라)
T = 10
for tc in range(1, T+1):
    n = int(input())
    # 100X100 2차원 리스트 만들기
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # pprint(ladder) # 왜 안되냐

    # x 좌표 찾아주기
    # 1. x의 row idx는 99야
    # 2. x의 col idx 찾아주기
    for i in range(100):
        if ladder[99][i] == 2:
            col = i
            break  # 찾았으면 멈춰!
    row = 99

    # 상,좌,우로 이동하고 좌,우에 1이 있으면 뱡향 바꿔서 좌,우로 직진
    # index error 방지
    # 0 <= [col - 1], [col + 1] <= 99 -> 0 < col < 99
    # 범위가 앞이고 == 이 뒤야!!!(단축평가)
    while row > 0:  # row가 0보다 클 때까지 반복(도착하면 row는 0이니까!)
        row -= 1  # row에서 1씩 빼면서 올라가
        if col > 0 and ladder[row][col - 1] == 1:  # 왼쪽이 1이면
            while col > 0 and ladder[row][col - 1] == 1:  # 왼쪽이 1일때까지 쭉쭉 이동해
                col -= 1
        elif col < 99 and ladder[row][col + 1] == 1:  # 오른쪽이 1이면
            while col < 99 and ladder[row][col + 1] == 1:  # 오른쪽이 1일때까지 쭉쭉 이동해
                col += 1

    print(f'#{tc} {col}')

