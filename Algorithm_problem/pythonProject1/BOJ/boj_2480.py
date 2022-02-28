# 간단한게 최고야..
A, B, C = map(int, input().split())
if A == B == C:
    print(10000 + A * 1000)
elif A == B:
    print(1000 + A * 100)
elif B == C:
    print(1000 + B * 100)
elif C == A:
    print(1000 + C * 100)
else:
    print(100 * max(A, B, C))

# lst = []
# lst.append(A)
# lst.append(B)
# lst.append(C)
# lst.sort(reverse=True)
# # print(lst)
# # if A == B == C:
# #     rlt = 10000 + (A*1000)
# #
# # elif A != B != C:
# #     rlt = lst[0] * 100
# #
# # else:
# #     if lst.count(A):
# #         rlt = 1000 + (A * 100)
# #     elif lst.count(B):
# #         rlt = 1000 + (B * 100)
# #     else:
# #         rlt = 1000 + (C * 100)
#
# for i in lst:
#     if lst.count(i) == 3:
#         rlt = 10000 + (i *1000)
#     elif lst.count(i) == 2:
#         rlt = 1000 + (i * 100)
#     else:
#         rlt = lst[0] * 100
#
# print(rlt)

