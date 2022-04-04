odd_lst = []
for _ in range(7):
    N = int(input())
    if N % 2:
        odd_lst.append(N)
odd_lst.sort()
total = 0
for i in odd_lst:
    total += i
if odd_lst:
    print(total)
    print(odd_lst[0])
else:
    print('-1')
