import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    memo = [0, 1, 3] # 이전 값 저장

    for i in range(3, n // 10 + 1):
        memo.append(memo[i - 1] + memo[i - 2]*2) # 점화식 : f(n) = f(n-1)+f(n-2)*2

    print(f'#{tc} {memo[-1]}')



