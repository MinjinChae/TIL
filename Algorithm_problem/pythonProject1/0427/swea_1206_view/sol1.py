# 문제 풀이의 포인트
# 조망권 확보를 위한 조건-> 왼쪽, 오른쪽 빌딩 2개씩 나보다 작아야해!(조건문 사용)
# 조망권 확보 빌딩 개수 -> 4개중에 가장 높은 빌딩 빼주기
import sys

sys.stdin = open('input.txt')

T = 10  # 테스트 케이스는 10개
for tc in range(1, T + 1):
    n = int(input())
    # 빌딩을 1차원 리스트로 입력 받기
    b_lst = list(map(int, input().split()))
# print(b_lst)
    cnt = 0  # 조망권 확보 빌딩 개수 0으로 초기화
    # 양쪽 2칸 공백 고려해서 순회하는 범위 지정 해주기
    for i in range(2, n - 2):
        # 만약에 나보다 왼쪽으로 두칸 떨어진 빌딩, 왼쪽 바로 옆 빌딩, 오른쪽으로 두칸 떨어진 빌딩, 오른쪽 바로 옆 빌딩이 작다면
        if b_lst[i] > b_lst[i - 2] and b_lst[i] > b_lst[i - 1] and b_lst[i] > b_lst[i + 1] and b_lst[i] > b_lst[i + 2]:
            # max 써서 얘네중에 제일 높은 애를 빼주자
            cnt += b_lst[i] - max(b_lst[i - 2], b_lst[i - 1], b_lst[i + 1], b_lst[i + 2])

    print(f'#{tc} {cnt}')

