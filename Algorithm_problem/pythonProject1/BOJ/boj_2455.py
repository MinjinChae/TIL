# 1. 이렇게 풀긴해도 맞았습니다 뜨긴 했는데..ㅎㅎ
n1, m1 = map(int, input().split())
n2, m2 = map(int, input().split())
n3, m3 = map(int, input().split())
n4, m4 = map(int, input().split())
lst = []
lst.append(m1)
lst.append(lst[0]-n2+m2)
lst.append(lst[1]-n3+m3)
lst.append(lst[2]-n4)
print(max(lst))

# 2.
total = 0
lst = []
for _ in range(4):
    n, m = map(int, input().split())
    total -= n
    total += m
    lst.append(total)
print(max(lst))
