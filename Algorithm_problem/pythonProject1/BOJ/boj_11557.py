# 딕셔너리로 풀기
T = int(input())
for tc in range(1, T+1):
    school = {}
    n = int(input())
    for _ in range(n):
        s, l = input().split()
        school[s] = int(l)
    swap_school = dict(zip(school.values(), school.keys()))
    print(swap_school[max(swap_school)])

# 리스트로 풀기
# = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     alcohol = []
#     for _ in range(n):
#         s, l = map(str, input().split())
#         alcohol.append([s, int(l)])
#     alcohol = sorted(alcohol, key=lambda x: x[1])
#     print(alcohol[-1][0])
T
