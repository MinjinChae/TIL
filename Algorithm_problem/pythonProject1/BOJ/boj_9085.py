# 1. for문으로 원소 하나씩 빼서 더해주기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    total = 0
    for i in num_lst:
        total += i
    print(f'{total}')

# 2. sum 함수 써서 더 간단하게 풀기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'{sum(list(map(int, input().split())))}')
