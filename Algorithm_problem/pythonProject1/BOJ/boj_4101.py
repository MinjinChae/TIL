n, m = map(int, input().split())

while n != 0 and m != 0:  # n,m 둘다 0이 아닐때까지 반복
    if n > m:
        print('Yes')
    else:
        print('No')
    n, m = map(int, input().split()) # 계속 반복적으로 input 받아줘야함