# 16진수 -> 2진수
# 10진수 -> 2진수 문자열로 바꿈
import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n, m  = map(int, input())

    print(f'#{tc} ')

