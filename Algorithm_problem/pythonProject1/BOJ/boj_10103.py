n = int(input())
score_a = 100
score_b = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        score_b -= a
    elif a < b:
        score_a -= b
    else:
        score_a = score_a
        score_b = score_b

print(score_a)
print(score_b)