# 첫 번째 방법
A, B = map(int, input().split())
while A != 0 and B != 0:
    print(A+B)
    A, B = map(int, input().split())

# 두 번째 방법
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A + B)