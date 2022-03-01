n = int(input())
while n != -1:
    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    if sum(lst) == n:
        print(n, " = ", " + ".join(str(i) for i in lst), sep="")
    else:
        print(n, "is NOT perfect.")
    n = int(input())

# 이것도 가능해!
while True:
    n = int(input())
    if n == -1:
        break
    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    if sum(lst) == n:
        print(n, " = ", " + ".join(str(i) for i in lst), sep="")
    else:
        print(n, "is NOT perfect.")

