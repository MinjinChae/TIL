import sys

sys.stdin = open('input.txt')

# 이진탐색 함수 정의
def binarysearch(pages, target): # pages: 전체 쪽 수 target: 찾는 쪽 수
    start = 1
    middle = 0
    cnt = 0 # 탐색 횟수 초기화
    end = pages
    while target != middle:
        middle = (start + end) // 2
        if middle > target:
            end = middle
        else:
            start = middle
        cnt += 1

    return cnt

T = int(input())

for tc in range(1, T + 1):
    p, pa, pb = map(int, input().split())

    A = binarysearch(p, pa)
    B = binarysearch(p, pb)
    result = 0
    if A < B:
        result = 'A'
    elif A > B:
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')

