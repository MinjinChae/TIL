import sys

sys.stdin = open('input7.txt')

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    number_lst = list(map(int, input().split()))
    new_lst = [] # 빈 리스트 만들어주기

    for i in range(n-m+1):  # 덧셈을 시작할 첫번째 idx
        sum_nums = 0
        for j in range(i, i+m):  # m 만큼의 구간
            sum_nums += number_lst[j]
        new_lst.append(sum_nums)

    # bubble sort로 오름차순 정렬
    for _ in range(len(new_lst)-1):
        for i in range(len(new_lst)-1):
            if new_lst[i] > new_lst[i+1]:
                new_lst[i], new_lst[i+1] = new_lst[i+1], new_lst[i]
    # new_lst[-1]: 가장 큰 수 new_lst[0]: 가장 작은 수
    print(f'#{tc} {new_lst[-1] - new_lst[0]}')

