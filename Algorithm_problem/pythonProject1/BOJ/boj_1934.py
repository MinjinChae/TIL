# 시간초과
# n = int(input())
# for _ in range(n):
#     a, b = map(int, input().split())
#     for i in range(max(a, b), (a * b) + 1):
#         if a % i == 0 and b % i == 0:
#         print(i)
#         break

# 유클리드 호제법 이용해서 풀기(1)
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    lcm = (a * b) // gcd
    print(lcm)

# # 유클리드 호제법 이용해서 풀기(2)
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    lcm = (a * b) // gcd
    print(lcm)
