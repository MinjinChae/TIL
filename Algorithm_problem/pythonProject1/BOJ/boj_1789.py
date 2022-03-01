# 1부터 n까지의 합 구하는 공식: n*(n+1)/2

s = int(input())
n = 1
while True:
    if n * (n+1) / 2 > s:
        break
    else:
        n += 1
print(n - 1)
