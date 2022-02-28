import sys

sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1, T + 1):
    tc = list(map(int, input().split()))
    max_num = 0  # 낙차가 가장 큰 상자의 낙차 초기화
    # 박스와 같거나 큰 박스 사이의 거리 구하기
    for i in range(T):
        cnt = 0
        for j in range(i+1, T):
            if tc[i] > tc[j]:
                cnt += 1
        if cnt > max_num:
            max_num = cnt

    print(f'#{tc} {max_num}')
