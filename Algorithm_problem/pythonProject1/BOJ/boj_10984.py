T = int(input())
for tc in range(1, T + 1):
    credit = 0
    total = 0
    N = int((input()))
    for _ in range(N):
        C, G = map(float, input().split())
        credit += C
        total += C * G
    gpa = total / credit
    print(int(credit), '%.1f' % gpa)
