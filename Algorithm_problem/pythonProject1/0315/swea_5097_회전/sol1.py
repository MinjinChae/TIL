import sys
sys.stdin = open('input.txt')

# deque 이용하면 popleft로 더 빠르게 할 수 있다고 그랬음..
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    # deque 라이브러리 사용
    queue = deque(list(map(int, input().split())))
    # 작업 횟수 cnt로 초기화
    cnt = 0
    # 작업 횟수가 m보다 작을 때 까지 반복하기
    while cnt < m:
        # 수열의 맨 앞에 있는 숫자 pop 해서 다시 수열에 추가해
        queue.append(queue.popleft())
        cnt += 1  # 작업 횟수 1 증가
    # 맨 앞에 있는 숫자 출력해야 하니까 pop.left 한 거 출력하기
    print(f'#{tc} {queue.popleft()}')

