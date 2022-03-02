M = int(input())
N = int(input())
lst = []
i = 1
while i ** 2 <= N:
    if M <= i ** 2 <= N:
        lst.append(i ** 2)
    i += 1
if lst == []:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])





