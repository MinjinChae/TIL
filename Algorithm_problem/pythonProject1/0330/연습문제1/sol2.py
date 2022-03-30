import sys

sys.stdin = open('input.txt')

def quick_sort(numbers, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and numbers[left] <= numbers[pivot]:
            left += 1
        while right > start and numbers[right] >= numbers[pivot]:
            right -= 1
        if left > right:
            numbers[right], numbers[pivot] = numbers[pivot], numbers[right]
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]

    quick_sort(numbers, start, right-1)
    quick_sort(numbers, right + 1, end)



T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, len(numbers) - 1)
    print(f'#{tc} {numbers}')


