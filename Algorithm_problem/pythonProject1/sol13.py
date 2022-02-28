import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    ans = 0
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            d_row = [-1, 1, 0, 0]
            d_col = [0, 0, -1, 1]
            for i in range(4):
                direct_r = r + d_row[i]
                direct_c = c + d_col[i]
                if direct_r < 0 or direct_r > 4 or direct_c < 0 or direct_c > 4 :
                    continue
                else:
                    sub = arr[r][c]





    direct
    print(f'#{tc} ')

