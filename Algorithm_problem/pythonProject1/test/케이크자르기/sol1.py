# point
# 가로 cut -> 위, 아래 딸기 갯수 같음
# 세로 cut -> 왼쪽, 오른쪽 딸기 갯수 같음
# 잘랐을 때 절반으로 나눌 수 있는지 확인하는 함수 작성

import sys

sys.stdin = open('input.txt')

def cut(arr):
    sum_rc = 0
    for i in range(n):
        sum_rc += sum(cake[i])
        if sum_rc * 2 == total: # 절반X2 를 했을 때 total이 되어야 함
            return True
    return False

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cake = [list(map(int, input().split())) for _ in range(n)]
    cake_trans = map(list, zip(*cake))
    total = 0 # 총 딸기 갯수 초기화
    for i in range(n):
        total += sum(cake[i])

    if cut(cake) and cut(cake_trans):
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')


