# 성진오빠 코드는 엄청 직관적이다..!
import sys

sys.stdin = open('input.txt')

def quick_sort(numbers):
    if len(numbers) <= 1:  # 리스트에 원소가 한개만 있으면 그냥 종료해!
        return numbers

    pivot = numbers[len(numbers) // 2]  # 피봇값은 리스트 맨 중간꺼
    less = []  # 피봇값보다 작은 수 담을 리스트
    more = []  # 피봇값보다 큰 수 담을 리스트
    equal = []  # 피봇값이랑 같은 수 담을 리스트

    for i in numbers:  # N개의 정수가 들어간 리스트를 하나씩 빼서
        if i < pivot:  # 피봇값보다 작으면 less 리스트에 넣어
            less.append(i)
        elif i > pivot:   # 피봇값보다 크면 more 리스트에 넣어
            more.append(i)
        else:   # 피봇값이랑 같으면 equal 리스트에 넣어
            equal.append(i)
    # quick_sort 함수에 의해 less, equal, more 이 나눠지잖아
    # 얘네 안에서 또 less, equal, more 나눠줘서 정렬해줘! -> 그래서 함수 쓰는거야
    # 그리고 합쳐주면 정렬 끝!
    return quick_sort(less) + equal + quick_sort(more)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{tc} {quick_sort(numbers)[N//2]}')

