import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    p = [[1], [1, 1]]
    for i in range(2, n):
        lst = [1]
        for j in range(i - 1):
            lst.append([p[i-1][j] + p[i-1][j+1]])
        lst += [1]
        p += [lst]

    for i in range(n):

        print(f'#{tc} {p[i]}')


