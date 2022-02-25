K, N, M = map(int, input().split())

if K * N > M:
    money = K * N - M
else:
    money = 0

print(money)