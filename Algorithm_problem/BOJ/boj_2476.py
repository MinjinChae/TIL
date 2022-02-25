n = int(input())
num_lst = []

for _ in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        num_lst.append(10000 + a * 1000)
    elif a == b:
        num_lst.append(1000 + a * 100)
    elif b == c:
        num_lst.append(1000 + b * 100)
    elif a == c:
        num_lst.append(1000 + a * 100)
    else:
        num_lst.append(100 * max(a, b, c))

print(max(num_lst))



# n = int(input())
# a1, b1, c1 = map(int, input().split())
# a2, b2, c2 = map(int, input().split())
# a3, b3, c3 = map(int, input().split())
# money = []
#
# lst1 = []
# lst1.append(a1)
# lst1.append(b1)
# lst1.append(c1)
#
# lst2 = []
# lst2.append(a2)
# lst2.append(b2)
# lst2.append(c2)
#
# lst3 = []
# lst3.append(a3)
# lst3.append(b3)
# lst3.append(c3)
#
# lst1.sort()
# lst2.sort()
# lst3.sort()
#
#
#
# if a1 == b1 == c1:
#     rlt = 10000 + a1 * 1000
#     money.append(rlt)
# elif a1 != b1 != c1:
#     rlt = 100 * max(lst1)
#     money.append(rlt)
# else:
#     rlt = 1000 + lst1[1] * 100
#     money.append(rlt)
#
#
# if a2 == b2 == c2:
#     rlt = 10000 + a2 * 1000
#     money.append(rlt)
# elif a2 != b2 != c2:
#     rlt = 100 * max(lst2)
#     money.append(rlt)
# else:
#     rlt = 1000 + lst2[1] * 100
#     money.append(rlt)
#
#
# if a3 == b3 == c3:
#     rlt = 10000 + a3 * 1000
#     money.append(rlt)
# elif a3 != b3 != c3:
#     rlt = 100 * max(lst3)
#     money.append(rlt)
# else:
#     rlt = 1000 + lst3[1] * 100
#     money.append(rlt)
#
# print(max(money))