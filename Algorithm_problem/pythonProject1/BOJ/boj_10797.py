day = int(input())
car_number = list(map(int, input().split()))
cnt = 0
for i in car_number:
    if i == day:
        cnt += 1
print(cnt)