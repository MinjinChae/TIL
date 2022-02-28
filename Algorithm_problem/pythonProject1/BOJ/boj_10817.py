A, B, C = map(int, input().split())
lst = []
lst.append(A)
lst.append(B)
lst.append(C)
lst.sort(reverse=True) #내림차순
print(lst[1])
