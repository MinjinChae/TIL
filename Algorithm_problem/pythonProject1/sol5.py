import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    ans = 0
    # 1. max 찾기
    max_num = n_list[0]
    for i in n_list:
        if i > max_num:
            max_num = i

    # 2. min 찾기
    min_num = n_list[0]
    for i in n_list:
        if i < min_num:
            min_num = i

    # 3. max_num-min_num
    ans = max_num-min_num

    print(f'#{tc} {ans}')

