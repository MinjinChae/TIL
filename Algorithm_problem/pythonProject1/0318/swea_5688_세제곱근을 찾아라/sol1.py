import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    ans = -1  # x가 존재하지 않을 때
    for i in range(1, n+1):
        if i * i * i > n:  # 세제곱 했을 때 n보다 커지면 멈춰!
            break
        if i * i * i == n:  # 세제곱 했을 때 n이면 x는 i야
            ans = i
            break  # 찾았으니까 멈춰!
    print(f'#{tc} {ans}')

