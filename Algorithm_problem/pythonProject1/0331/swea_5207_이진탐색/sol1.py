import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_lst = sorted(list(map(int, input().split())))
    M_lst = list(map(int, input().split()))
    cnt = 0

    for i in range(N):
        l = 0
        r = N - 1
        target  = M_lst[i]
        while l <= r:
            mid = (l + r) // 2
            if target == N_lst[i]:
                cnt += 1
            elif target > M_lst[mid]:

            elif target < M_lst[mid]:


    print(f'#{tc} ')

