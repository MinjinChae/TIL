import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    n_lst = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(0, n-m+1):
            if n_lst[i][j:j+m] == n_lst[i][j:j+m][::-1]:
                print(f'#{tc} {"".join(n_lst[i][j:j+m])}')



