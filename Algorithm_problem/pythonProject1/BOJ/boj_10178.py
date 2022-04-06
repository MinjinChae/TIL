T = int(input())
for tc in range(1, T+1):
    c, v = map(int,input().split())
    a = c // v
    b = c % v
    print(f'You get {a} piece(s) and your dad gets {b} piece(s).')
