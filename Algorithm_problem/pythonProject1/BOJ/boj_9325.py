T = int(input())
for tc in range(1, T + 1):
    s = int(input())
    n = int(input())
    for _ in range(n):
        q, p = map(int, input().split())
        s += (q * p)
    print(s)


