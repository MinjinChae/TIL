# 문제 풀이의 포인트
# 가장 높은 상자에서 상자 하나를 가장 낮은 상자로 옮기기 때문에
# 가장 높은 상자 -= 1, 가장 낮은 상자 += 1  상자 리스트는 이 상태로 갱신됨
# 덤프 횟수 끝 -> 평탄화 완료 -> 가장 높은 상자 - 가장 낮은 상자
import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    dump = int(input())  # 덤프 횟수
    box_height = list(map(int, input().split()))  # 상자의 높이들

    # 덤프 횟수만큼 반복
    for _ in range(dump):
        # 가장 높은 박스, 가장 낮은 박스 구하기
        max_box = max(box_height)
        min_box = min(box_height)
        # 가장 높은 박스의 idx, 가장 낮은 박스의 idx 구하기 -> list.index() 사용해
        max_idx = box_height.index(max_box)
        min_idx = box_height.index(min_box)
        # 가장 높은 박스는 1 빼주고 가장 낮은 박스는 1 더해주기
        box_height[max_idx] -= 1
        box_height[min_idx] += 1
        # box_height가 평탄화 작업이 이루어지고 다시 위로 올라감(box_height는 갱신 된 상태)

    # testcase 9/10
    # print(f'#{tc} {max_box - min_box}')
    print(f'#{tc} {max(box_height) - min(box_height)}')

