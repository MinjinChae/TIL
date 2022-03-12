n, x = map(int, input().split())
n_lst = list(map(int, input().split()))
for i in range(n):
    if n_lst[i] < x:
        print(n_lst[i], end=" ")