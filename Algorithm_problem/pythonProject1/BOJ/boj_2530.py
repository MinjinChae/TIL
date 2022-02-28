h, m, s = map(int, input().split())
time = int(input())

m += time // 60
s += time % 60

while s >= 60:
    m += 1
    s -= 60

while m >= 60:
    h += 1
    m -= 60

while h >= 24:
    h -= 24

print(h, m, s)
