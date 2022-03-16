import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    n = int(input())
    tree = [[0] * 4 for _ in range(n+1)]
    for _ in range(n):
        lst = list(input().split())
        if lst[1].isdigit():
            tree[int(lst[0])][1] = int(lst[1])
        else:
            tree[int(lst[0])][1] = lst[1]
            tree[int(lst[0])][2] = int(lst[2])
            tree[int(lst[0])][3] = int(lst[3])



    print(f'#{tc} ')

