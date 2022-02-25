import sys

sys.stdin = open('input.txt')

T = int(input())

def pattern(str1, str2):
    N = len(str1)
    M = len(str2)

    for i in range(M-N+1):
        cnt = 0
        for j in range(N):
            if str2[i+j] == str1[j]:
                cnt += 1
                if cnt == N:
                    return 1
    return 0

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = pattern(str1, str2)

    print(f'#{tc} {result}')

