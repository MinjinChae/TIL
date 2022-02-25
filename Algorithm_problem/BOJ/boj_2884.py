h, m = map(int, input().split())

if m > 44:
    h = h
    m -= 45

elif h == 0 and m < 45:
    h = 23
    m += 15

else:
    h -= 1
    m += 15

print(h, m)