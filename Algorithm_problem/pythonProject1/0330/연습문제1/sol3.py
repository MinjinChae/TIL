# 구글링 찬스..헤헤...
import sys

sys.stdin = open('input.txt')
# start: 처음 idx end: 끝 idx
def quick_sort(numbers, start, end):
    if start >= end:  # 원소가 1개면 그냥 종료해!
        return
    pivot = start   # 피벗을 처음 원소로 지정
    left = start + 1  # numbers[pivot]보다 큰 값인 left idx
    right = end  # numbers[pivot]보다 작은 값인 right idx
    # 엇갈리기전까지 반복해(왼쪽에서 출발한게 오른쪽에서 출발한 것 보다 작을때까지)
    while left <= right:
        # 피벗보다 큰 수 찾을 때까지 반복해
        while left <= end and numbers[left] <= numbers[pivot]:
            left += 1
        # 피벗보다 작은 수 찾을 때까지 반복해
        while right > start and numbers[right] >= numbers[pivot]:
            right -= 1

        # 엇갈렸으면 작은 수랑 피벗 위치 바꿔
        if left > right:
            numbers[right], numbers[pivot] = numbers[pivot], numbers[right]
        # 그게 아니라면 작은 수랑 큰 수 위치 바꿔
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]

    # 분할하고 왼쪽, 오른쪽 각각 퀵 정렬 함수 실행해!
    quick_sort(numbers, start, right-1)
    quick_sort(numbers, right + 1, end)



T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, len(numbers) - 1)
    print(f'#{tc} {numbers}')

