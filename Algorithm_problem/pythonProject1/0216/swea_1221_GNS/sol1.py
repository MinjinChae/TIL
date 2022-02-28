import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int,input().split()))
    number_alpha = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    bucket = [0] * 10
    for i in range(len(arr)):
        for j in range(len(number_alpha)):
            if arr[i] == number_alpha[j]:
                bucket[j] += 1

    for i in range(len(bucket)):
        for _ in range(bucket[i]):
            print(f'#{tc} {number_alpha[i]}', end ='')
    print()

